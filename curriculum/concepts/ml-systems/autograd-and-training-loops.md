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

## Exercise Bridge

ML systems exercises should make tensors, autograd, optimizers, training loops, checkpointing, and inference serving explicit. Before implementing, write down the forward value each operation saves for its backward rule.

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
