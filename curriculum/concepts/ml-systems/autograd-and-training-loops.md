# Autograd and Training Loops

## What You Should Know First

You should know basic functions, arrays or tensors, and the idea that model training adjusts parameters to reduce a loss value. You do not need advanced calculus, but the chain rule will appear.

## The Problem

Machine learning models can have millions or billions of parameters. Manually deriving and coding every gradient would be brittle. Autograd systems record the computation that produced a value, then compute gradients backward through that graph.

Training loops use those gradients to update parameters repeatedly over data.

## Vocabulary

| Term | Meaning |
| --- | --- |
| Tensor | Multidimensional numeric array. |
| Parameter | Tensor the optimizer updates during training. |
| Loss | Scalar value measuring how wrong the model is. |
| Gradient | Derivative of loss with respect to a value. |
| Computational graph | Operations and dependencies that produced an output. |
| Backpropagation | Reverse traversal that applies the chain rule. |
| Optimizer | Algorithm that updates parameters from gradients. |

## Mental Model

The forward pass builds a recipe:

```text
x -> multiply -> add -> loss
```

The backward pass walks the recipe in reverse:

```text
loss gradient -> add gradient -> multiply gradient -> parameter gradients
```

Each operation knows how to pass gradient information to its inputs.

## How It Works Step By Step

Autograd is a bookkeeping system for the chain rule.

| Step | What Happens | Why It Matters |
| --- | --- | --- |
| Create tensors | Values may or may not require gradients. | The engine knows what to track. |
| Run forward ops | Each operation computes output data. | The model produces a prediction and loss. |
| Record parents | Outputs remember which inputs created them. | The graph can be traversed backward. |
| Store backward rule | Each op knows local derivatives. | Gradients can be propagated. |
| Topologically sort | Nodes are ordered from loss back to leaves. | Parents receive complete downstream gradients. |
| Accumulate gradients | Contributions from multiple paths are added. | Shared values train correctly. |
| Optimizer step | Parameters are updated and gradients cleared. | Training moves to the next iteration. |

The graph is a temporary explanation of one computation. The parameters are the long-lived state being trained.

## Core Invariant

For every differentiable operation, the backward rule must propagate gradients that match the forward computation's local derivative and tensor shapes.

Wrong gradients can be worse than crashes because training may continue while silently learning the wrong thing.

## Worked Example

Let:

```text
y = w * x + b
loss = (y - target)^2
```

| Value | Role |
| --- | --- |
| `w`, `b` | Parameters to update. |
| `x` | Input. |
| `target` | Desired output. |
| `loss` | Scalar error. |

Autograd records multiplication, addition, subtraction, and square operations. Backward computes how much changing `w` or `b` would change the loss. The optimizer then nudges `w` and `b` in the direction that reduces loss.

## State Or Flow Walkthrough

For:

```text
y = w * x + b
loss = (y - target)^2
```

The backward pass starts with `d loss / d loss = 1`. The square operation sends gradient to `(y - target)`. The subtraction sends gradient to `y`. The addition sends gradient to `w * x` and `b`. The multiplication sends gradient to `w` and `x`.

If `w` appears in two branches of the graph, both branches contribute to `w.grad`. Assigning instead of accumulating silently loses learning signal.

## Implementation Shape

A tiny autograd engine usually has:

| Piece | Responsibility |
| --- | --- |
| Tensor object | Stores data, gradient, and graph metadata. |
| Operation node | Stores parents and backward function. |
| Topological sort | Orders graph nodes for reverse traversal. |
| Backward pass | Accumulates gradients into parents. |
| Optimizer | Updates parameters and clears gradients. |
| Training loop | Batches data, runs forward, computes loss, backward, and step. |

Gradient accumulation is intentional. If a value feeds two downstream paths, both gradient contributions must be added.

## Failure Modes

| Failure | Symptom |
| --- | --- |
| Shape mismatch in backward | Runtime errors or incorrect broadcasting. |
| Forgetting to zero gradients | Updates include stale gradients from earlier batches. |
| No topological order | Backward uses gradients before they are complete. |
| In-place mutation | Saved forward values are corrupted. |
| Exploding gradients | Training becomes unstable. |
| No checkpointing | Long training jobs lose progress on failure. |

## Exercise Mapping

| Exercise | Concept Piece It Uses |
| --- | --- |
| Autograd engine | Tensor graph construction, topological backward, gradient accumulation. |
| Mini deep learning framework | Modules, parameters, losses, optimizers, and training loops. |
| Distributed training simulator | Checkpointing, gradient synchronization, and failure recovery. |
| Inference server | Separates training-time graph concerns from serving-time latency and batching. |

## Exercise Bridge

ML systems exercises should make tensors, autograd, optimizers, training loops, checkpointing, and inference serving explicit. Before implementing, write down the forward value each operation saves for its backward rule.

## Readiness Checklist

You are ready for ML systems exercises when you can:

- draw the computation graph for a small expression
- explain why backward runs in reverse topological order
- distinguish parameter data from gradient data
- explain why gradients accumulate
- say what a checkpoint must save to resume training

## Self-Check

1. Why does backward traverse the graph in reverse?
2. When should gradients be accumulated instead of assigned?
3. Why must loss usually be scalar for a simple backward call?
4. What state should a checkpoint save?
5. How can a model train without actually learning?

## Further Reading

- micrograd: https://github.com/karpathy/micrograd
- PyTorch autograd mechanics: https://pytorch.org/docs/stable/notes/autograd.html
- Deep Learning book, backpropagation chapter: https://www.deeplearningbook.org/contents/mlp.html
