# Chapter 2: Networking and Distributed Systems

This chapter moves from one machine to many. It starts with protocol parsing and connection lifecycles, then builds toward routing, reliable transport, goroutine ownership, consensus, replication, sharding, and stream processing.

**Chapter promise:** The learner should leave this chapter with a sharper instinct for ambiguity: packets disappear, clocks drift, goroutines leak, leaders change, and retries can mutate state twice unless the design prevents it.

## Chapter Map

| Domain | Projects | What This Domain Trains |
| --- | ---: | --- |
| Networking | 3 | Networking starts with one connection at a time: parsing, timeouts, lifecycle, backpressure, and protocol correctness. |
| Deep Networking | 5 | Deep networking projects expose the machinery below application protocols: forwarding, translation, retransmission, routing convergence, and congestion signals. |
| Go Concurrency | 1 | Go concurrency is the bridge from local programs to services. The emphasis is ownership, cancellation, bounded work, and leak-free shutdown. |
| Distributed Systems | 4 | Distributed systems work asks the learner to design around ambiguity. The projects force explicit thinking about replication, leadership, idempotency, and failure models. |

## Networking

Networking starts with one connection at a time: parsing, timeouts, lifecycle, backpressure, and protocol correctness.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| HTTP Server From Scratch | Build an HTTP/1.1 server with request parsing, keep-alive, routing, static files, chunked encoding, and graceful shutdown. | protocol parsing<br>connection lifecycle<br>timeouts<br>streaming<br>request smuggling risks | fuzz the parser<br>handle slowloris-style clients<br>separate protocol errors from application errors<br>expose connection metrics |
| DNS Resolver | Build a recursive-ish resolver with packet encoding/decoding, cache TTLs, retries, and UDP/TCP fallback. | binary protocols<br>caching<br>retries and timeouts<br>recursive resolution<br>negative caching | test malformed packets<br>avoid cache poisoning basics<br>expose cache hit rate and latency |
| Layer 4 Load Balancer | Build a TCP load balancer with health checks, connection draining, least-connections, and consistent hashing. | proxying<br>health checks<br>load distribution<br>graceful deploys<br>observability | handle backend flapping<br>preserve half-close behavior<br>test under many concurrent connections |

## Deep Networking

Deep networking projects expose the machinery below application protocols: forwarding, translation, retransmission, routing convergence, and congestion signals.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Reliable Transport From Scratch | Build a TCP-like protocol over an unreliable packet interface with sequence numbers, ACKs, retransmission, flow control, and congestion-control basics. | packet loss and reordering<br>reliable delivery<br>sliding windows<br>retransmission timers<br>flow versus congestion control | test duplicate/lost/reordered packets<br>avoid delivering bytes twice<br>model timeouts as uncertainty<br>benchmark throughput under loss |
| IP Router Lab | Build a router that handles Ethernet frames, ARP, IPv4 forwarding, longest-prefix match, TTL, ICMP errors, and routing-table updates. | packet forwarding<br>ARP<br>routing tables<br>checksums<br>ICMP | test malformed packets<br>explain every dropped packet<br>avoid routing loops<br>expose forwarding counters |
| NAT Gateway | Build a NAT that tracks connections, rewrites addresses/ports, expires mappings, and handles TCP/UDP differences. | connection tracking<br>address translation<br>ephemeral ports<br>timeout policies<br>stateful middleboxes | handle port exhaustion<br>test mapping expiry<br>expose conntrack metrics<br>reason about protocols that dislike NAT |
| Dynamic Routing Simulator | Build distance-vector and link-state routing simulations with topology changes, route convergence, and failure injection. | routing protocols<br>convergence<br>count-to-infinity<br>link-state flooding<br>failure detection | visualize convergence<br>detect routing loops<br>compare protocols under churn |
| QUIC-Like Reliable UDP Transport | Build a simplified QUIC-inspired transport with streams, connection IDs, retransmission, and handshake state. | multiplexed streams<br>connection migration intuition<br>head-of-line blocking<br>packet number spaces<br>encrypted transport boundaries | isolate stream failures<br>test packet reordering<br>measure tail latency versus TCP-like design |

## Go Concurrency

Go concurrency is the bridge from local programs to services. The emphasis is ownership, cancellation, bounded work, and leak-free shutdown.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Go Concurrency Gauntlet | Build worker pools, cancellable pipelines, bounded queues, singleflight caches, pub/sub brokers, actors, crawlers, and a MapReduce runtime. | goroutine ownership<br>channel closing<br>cancellation<br>backpressure<br>race freedom<br>leak detection | run `go test -race`<br>add stress tests<br>avoid sleep-based tests<br>expose goroutine and queue metrics |

## Distributed Systems

Distributed systems work asks the learner to design around ambiguity. The projects force explicit thinking about replication, leadership, idempotency, and failure models.

| Project | What You Build | Core Concepts | Staff-Level Pressure |
| --- | --- | --- | --- |
| Replicated WAL With Raft | Build a local durable log, then replicate it with Raft leader election, log replication, snapshots, and membership changes. | consensus<br>terms and epochs<br>quorum commit<br>crash recovery<br>deterministic simulation | separate safety and liveness<br>simulate partitions and restarts<br>test stale leaders<br>instrument commit lag and election churn |
| Dynamo-Style KV Store | Build a highly available key-value store with consistent hashing, sloppy quorums, hinted handoff, vector clocks, and read repair. | availability/consistency tradeoffs<br>conflict resolution<br>anti-entropy<br>quorum tuning<br>operational SLAs | make conflicts visible to clients<br>test network partitions<br>compare with Raft semantics<br>expose divergence metrics |
| MapReduce Runtime | Build a local then distributed MapReduce engine with task scheduling, shuffle, retries, speculative execution, and worker failure handling. | data parallelism<br>partitioning<br>fault-tolerant execution<br>deterministic task outputs<br>scheduling | retry idempotently<br>handle partial task outputs<br>add progress tracking<br>benchmark skewed workloads |
| Stream Processor | Build a mini Kafka/Flink-like system with partitions, offsets, consumer groups, checkpoints, and windowed aggregation. | ordered logs<br>replay<br>consumer offsets<br>checkpointing<br>event time versus processing time | define delivery semantics<br>test rebalances<br>handle poison messages<br>expose lag and checkpoint age |

## How To Use This Chapter

| Move | What The Learner Should Do | Evidence To Produce |
| --- | --- | --- |
| Learn the concept | Read the relevant concept chapter before opening the code. | A short note naming the invariant and the failure mode. |
| Implement the milestone | Fill the placeholder implementation for the current exercise only. | A passing validator for that milestone. |
| Review like a Staff engineer | Inspect edge cases, recovery behavior, observability, and test strength. | A design note explaining what the tests prove and what they do not prove. |
