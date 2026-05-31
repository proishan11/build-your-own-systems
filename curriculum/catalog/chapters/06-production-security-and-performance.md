# Chapter 6: Production, Security, and Performance

This chapter is about judgment under pressure. The learner builds systems that must survive overload, attacks, rollout mistakes, confusing dashboards, secret exposure, and misleading benchmark results.

**Chapter promise:** The learner should practice evidence-driven engineering: define the invariant, observe the system, form a hypothesis, make a small change, and prove whether the system became safer, faster, or more reliable.

## Chapter Map

| Domain | Projects | What This Domain Trains |
| --- | ---: | --- |
| System Design and SRE | 3 | System design and SRE projects connect architecture to operations: rate limits, rollouts, observability, incidents, and reliability tradeoffs. |
| Security Engineering | 5 | Security projects train adversarial thinking. The goal is not only to patch bugs, but to design boundaries that make whole classes of mistakes harder. |
| Performance Engineering | 5 | Performance projects teach measurement discipline. The learner must distinguish throughput, tail latency, lock contention, profiling signal, and benchmark noise. |

## System Design and SRE

System design and SRE projects connect architecture to operations: rate limits, rollouts, observability, incidents, and reliability tradeoffs.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Rate-Limited API Gateway | Build an API gateway with auth, rate limits, circuit breakers, request hedging, retries, and observability. | overload control<br>fairness<br>tail latency<br>failure containment<br>idempotency | avoid retry storms<br>define per-tenant fairness<br>test dependency outages |
| Observability Stack | Build metrics, logs, traces, RED/USE dashboards, alerts, and incident notebooks around one of the systems above. | telemetry<br>alert design<br>tracing<br>SLOs<br>incident response | alert on symptoms, not noise<br>make debugging paths obvious<br>run game days |
| Feature Flag and Rollout System | Build flags, targeting, gradual rollout, kill switches, audit logs, and experiment analysis. | configuration distribution<br>consistency<br>blast-radius control<br>auditability<br>product experimentation | handle stale clients<br>support emergency rollback<br>prevent unsafe flag combinations |

## Security Engineering

Security projects train adversarial thinking. The goal is not only to patch bugs, but to design boundaries that make whole classes of mistakes harder.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Vulnerable Web App Lab | Build a deliberately vulnerable application, exploit it, then fix it with tests. | injection<br>broken access control<br>session flaws<br>insecure deserialization<br>security regression testing | write exploit proofs<br>add tests that prevent reintroduction<br>log security-relevant events<br>document trust boundaries |
| Auth and Session System | Build authentication, password storage, sessions, CSRF protection, MFA hooks, and authorization checks. | identity<br>password hashing<br>sessions<br>authorization<br>CSRF/XSS boundaries | rotate sessions on privilege change<br>test confused-deputy cases<br>audit admin actions<br>model account recovery risk |
| Secrets Manager | Build a local secrets manager with envelope encryption, access policies, audit logs, rotation, and lease-based credentials. | encryption at rest<br>key hierarchy<br>access control<br>rotation<br>auditability | prevent plaintext leaks in logs<br>implement least privilege<br>test rotation failure modes<br>model compromise recovery |
| Supply-Chain Scanner | Build a scanner that reads dependency manifests, checks known-vulnerability feeds, verifies checksums/signatures, and emits policy results. | dependency metadata<br>vulnerability matching<br>provenance<br>SBOMs<br>policy-as-code | distinguish vulnerable from reachable<br>handle false positives<br>generate actionable reports<br>gate builds with explainable policy |
| Agent Security Lab | Build attacks and defenses for prompt injection, tool abuse, data exfiltration, malicious documents, and unsafe tool outputs. | LLM threat models<br>tool trust boundaries<br>retrieval poisoning<br>sandboxing<br>approval gates | add red-team fixtures<br>separate untrusted data from instructions<br>require approval for mutating tools<br>trace every security decision |

## Performance Engineering

Performance projects teach measurement discipline. The learner must distinguish throughput, tail latency, lock contention, profiling signal, and benchmark noise.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Profiler From Scratch | Build a sampling profiler that captures stack traces, aggregates hot paths, and renders a simple flamegraph-like report. | sampling<br>stack unwinding intuition<br>CPU attribution<br>profiler overhead<br>visualization | measure profiler overhead<br>compare sampled versus instrumented timing<br>handle short-lived functions<br>make results reproducible |
| Tail Latency Lab | Build a service with controlled sources of latency: queues, locks, GC pressure, slow dependencies, and retry storms. | p50/p95/p99<br>queueing<br>contention<br>load shedding<br>timeout budgets | show histograms<br>isolate root causes<br>prevent coordinated retry storms<br>validate improvements under load |
| Lock Contention Lab | Build workloads around global locks, sharded locks, lock-free-ish structures, and read/write locks. | contention<br>critical sections<br>fairness<br>starvation<br>profiling locks | prove contention with evidence<br>benchmark under varying cores<br>explain throughput versus latency<br>avoid premature cleverness |
| Benchmark Harness | Build a harness for repeatable benchmarks, warmup, workload definitions, confidence intervals, and regression reports. | experimental design<br>workload modeling<br>variance<br>regression detection<br>performance reporting | record environment metadata<br>detect noisy runs<br>compare against baselines<br>prevent benchmark gaming |
| Observability With eBPF Concepts | Build a lab that traces syscalls, network connections, latency, and process behavior using available platform tooling or simulated eBPF probes. | kernel-level observability<br>low-overhead tracing<br>syscall visibility<br>production debugging | minimize overhead<br>avoid leaking sensitive data<br>connect low-level signals to user-visible symptoms |

## How To Use This Chapter

| Move | What The Learner Should Do | Evidence To Produce |
| --- | --- | --- |
| Learn the concept | Read the relevant concept chapter before opening the code. | A short note naming the invariant and the failure mode. |
| Implement the milestone | Fill the placeholder implementation for the current exercise only. | A passing validator for that milestone. |
| Review like a Staff engineer | Inspect edge cases, recovery behavior, observability, and test strength. | A design note explaining what the tests prove and what they do not prove. |
