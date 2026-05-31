# Reconciliation and Controllers

## Concept

Reconciliation is the loop that compares desired state with observed state and takes action to reduce the difference. Kubernetes controllers are reconciliation loops over API objects.

## Why It Exists

Distributed infrastructure is constantly changing: pods crash, nodes disappear, images fail to pull, humans edit configuration, and network calls time out. A controller does not assume one command succeeds forever. It keeps observing and nudging reality toward the declared goal.

## Mental Model

```text
desired state + observed state -> diff -> action -> observe again
```

A Deployment controller sees "I want three replicas" and "only two are running," then creates another Pod. If too many exist, it deletes one.

## Core Invariant

The controller should make progress toward desired state while keeping every action safe to retry.

## Tiny Example

A custom resource says:

```yaml
spec:
  replicas: 3
```

The controller lists child pods and finds two healthy pods. It creates one more. If the create call times out, it cannot assume failure; it must observe again.

## Common Misconceptions

- A controller is not a one-shot script.
- Timeouts do not prove an operation failed.
- Status is part of the user experience, not an afterthought.
- Idempotency matters because reconciliation repeats.
- Permissions are design, not plumbing.

## Self-Check

1. What is desired state?
2. What is observed state?
3. Which operations are safe to retry?
4. What status should users see?
5. What permissions does the controller really need?

## Further Reading

- Kubernetes controllers: https://kubernetes.io/docs/concepts/architecture/controller/
- Kubernetes operator pattern: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
- Kubernetes docs: https://kubernetes.io/docs/

