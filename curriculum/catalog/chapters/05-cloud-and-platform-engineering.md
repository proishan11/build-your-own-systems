# Chapter 5: Cloud and Platform Engineering

This chapter studies isolation and reconciliation. Containers explain how processes are packaged and constrained; Kubernetes explains how desired state is observed, compared, retried, and repaired.

**Chapter promise:** The learner should be able to reason about platform systems as control loops: every controller needs a state model, a diff, idempotent actions, failure handling, and observability.

## Chapter Map

| Domain | Projects | What This Domain Trains |
| --- | ---: | --- |
| Kubernetes | 4 | Kubernetes projects teach reconciliation: observe state, compare it with intent, choose a safe action, and repeat under partial failure. |
| Containers | 3 | Container projects explain how images, registries, namespaces, and process isolation fit together below orchestration. |

## Kubernetes

Kubernetes projects teach reconciliation: observe state, compare it with intent, choose a safe action, and repeat under partial failure.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Kubernetes Controller From Scratch | Build a controller that watches a custom resource and reconciles child resources. | Kubernetes API model<br>watches and informers<br>desired versus observed state<br>idempotent reconciliation<br>status conditions | handle retries safely<br>set owner references<br>update status clearly<br>use minimal RBAC |
| Operator for PostgreSQL Backups | Build an operator that schedules backups, records status, verifies restores, and alerts on missed recovery objectives. | CRDs<br>controllers<br>backup orchestration<br>secrets<br>operational runbooks | test restore, not just backup<br>handle stuck jobs<br>model RPO/RTO<br>add disaster-recovery drills |
| Admission Controller | Build a validating/mutating admission webhook for image policies, resource limits, labels, and security context. | admission flow<br>policy enforcement<br>TLS/webhooks<br>failure policy<br>cluster security | avoid blocking the cluster during outages<br>report actionable errors<br>test policy bypass attempts |
| Scheduler Simulator | Build a scheduler that assigns pods to nodes using resource requests, affinity, taints, topology spread, and preemption. | bin packing<br>constraints<br>fairness<br>preemption<br>scheduling explainability | show why scheduling failed<br>simulate large clusters<br>test fragmented capacity |

## Containers

Container projects explain how images, registries, namespaces, and process isolation fit together below orchestration.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Mini Container Runtime | Build a runtime using Linux namespaces, cgroups, mounts, capabilities, seccomp, and an OCI-style bundle. | process isolation<br>filesystem isolation<br>resource limits<br>container lifecycle<br>security boundaries | drop capabilities<br>isolate mounts<br>enforce memory/CPU limits<br>explain what is not isolated |
| OCI Image Builder | Build a simple image builder that creates layers, config, manifests, and content-addressed blobs. | image layers<br>digests<br>registries<br>reproducibility<br>caching | make builds reproducible<br>verify digests<br>implement layer cache invalidation |
| Container Registry | Build a small OCI-compatible registry subset with blob upload, manifest push/pull, auth, and garbage collection. | content-addressed storage<br>HTTP APIs<br>auth<br>garbage collection<br>distribution semantics | handle interrupted uploads<br>prevent deleting referenced blobs<br>expose storage metrics |

## How To Use This Chapter

| Move | What The Learner Should Do | Evidence To Produce |
| --- | --- | --- |
| Learn the concept | Read the relevant concept chapter before opening the code. | A short note naming the invariant and the failure mode. |
| Implement the milestone | Fill the placeholder implementation for the current exercise only. | A passing validator for that milestone. |
| Review like a Staff engineer | Inspect edge cases, recovery behavior, observability, and test strength. | A design note explaining what the tests prove and what they do not prove. |
