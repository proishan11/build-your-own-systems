# Reconciliation and Controllers

## What You Should Know First

You should know that Kubernetes stores desired state as API objects and that real systems drift: pods crash, nodes disappear, images fail to pull, and humans change things manually.

## The Problem

A platform cannot assume one command will make reality match intent forever. Distributed infrastructure changes continuously. Reconciliation solves this by running a loop that observes current state, compares it to desired state, and takes small idempotent actions.

Controllers are the programs that run these loops.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Desired state | What the API object says should exist. |
| Observed state | What the controller sees in the cluster or external system. |
| Reconcile loop | Read, compare, act, and requeue. |
| Controller | Process responsible for reconciling one or more resource types. |
| CRD | Custom Resource Definition, an extension to the Kubernetes API. |
| Finalizer | Marker that lets a controller clean up external resources before deletion completes. |
| Idempotent action | An action that is safe to retry. |

## Mental Model

A controller is a thermostat:

```text
desired temperature -> observe room -> heat or cool -> observe again
```

It does not assume one action fixes the world permanently. It keeps checking. If an action fails, it records enough state to try again safely.

## How It Works Step By Step

A controller turns a desired-state API into repeated repair work.

| Step | Controller Question | Typical Output |
| --- | --- | --- |
| Watch | Which object changed or needs retry? | A key enters the work queue. |
| Fetch | Does the object still exist? | Current desired state or deletion path. |
| Observe | What child resources or external resources exist? | Observed state snapshot. |
| Diff | What is missing, extra, or stale? | A small operation plan. |
| Act | Which idempotent action should run now? | Create, patch, delete, or external API call. |
| Record status | What did the controller learn? | Conditions, observed generation, error reason. |
| Requeue | Should this be checked again? | Immediate retry, delayed retry, or done. |

The controller is successful when repeated reconciliation is safe. It does not need every API call to succeed the first time.

## Core Invariant

Each reconcile pass should move the system closer to desired state or record a clear reason why it cannot, without making retries unsafe.

This is why idempotency matters. Controllers often see the same object many times.

## Worked Example

Suppose a custom resource says:

```text
Backup name=daily users-db schedule=02:00 retention=7
```

| Reconcile Step | Controller Question |
| --- | --- |
| Read object | What backup does the user want? |
| Observe jobs | Does a matching CronJob already exist? |
| Diff | Is the existing job missing or out of date? |
| Act | Create or patch the CronJob. |
| Status | Record last observed state and errors. |

If the create call times out, the controller must not blindly create duplicates on retry. It should observe again first.

## State Or Flow Walkthrough

A `PostgresBackup` object asks for a daily backup job.

```text
spec: schedule=02:00 retention=7 target=users-db
observed: no CronJob exists
plan: create CronJob owned by PostgresBackup
act: create CronJob
status: Ready=False, Reason=JobCreated
next observe: CronJob exists with expected spec
status: Ready=True
```

If the create call times out, the next reconcile should observe before creating again. The timeout means uncertainty, not proof that creation failed.

## Implementation Shape

A controller implementation usually has:

| Piece | Responsibility |
| --- | --- |
| Watch/cache | Notices resource changes and queues keys. |
| Reconcile function | Handles one object key at a time. |
| Desired builder | Converts spec into desired child resources or external calls. |
| Diff planner | Compares desired and observed state. |
| Action executor | Creates, patches, deletes, or calls external APIs. |
| Status updater | Records conditions, versions, and errors. |

Good controllers are boring in the best way: deterministic diffs, explicit status, safe retries, and good events.

## Failure Modes

| Failure | Result |
| --- | --- |
| Non-idempotent create | Retries duplicate external resources. |
| No status conditions | Operators cannot tell what happened. |
| Ignoring deletion/finalizers | External resources leak. |
| Acting on stale assumptions | Controller fights other actors. |
| Requeue storm | A failing object burns CPU and API quota. |

## Exercise Mapping

| Exercise | Concept Piece It Uses |
| --- | --- |
| Kubernetes controller project ladder | Desired/observed state, deterministic diffs, safe actions, and status conditions. |
| Operator for PostgreSQL backups | External resource ownership, retry safety, finalizers, and operational status. |
| Admission controller and scheduler labs | Policy boundaries and control-plane decision points. |

## Exercise Bridge

Kubernetes controller exercises use this concept directly: state model, operation planner, failure recovery, and integration simulation are all pieces of reconciliation. Before coding, define desired state, observed state, action set, and retry behavior.

## Readiness Checklist

You are ready to implement controller exercises when you can:

- define desired state and observed state separately
- list actions that are safe to retry
- explain what status condition helps an operator
- handle deletion and cleanup without leaking resources
- avoid duplicate external resources after timeout

## Self-Check

1. What does the controller own?
2. Which actions are safe to retry?
3. What status would help an operator debug failure?
4. How does deletion cleanup work?
5. What prevents the controller from creating duplicate external resources?

## Further Reading

- Kubernetes controller pattern docs: https://kubernetes.io/docs/concepts/architecture/controller/
- Kubebuilder book: https://book.kubebuilder.io/
- Kubernetes API conventions: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md
