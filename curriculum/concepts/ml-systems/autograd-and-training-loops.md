# Autograd and Training Loops

## Concept

Automatic differentiation records or reconstructs the operations that produced a value, then applies the chain rule backward to compute gradients for model parameters.

## Why It Exists

Modern machine learning depends on optimizing huge numbers of parameters. Manually deriving and coding every gradient is error-prone. Autograd lets model authors express computation while the system computes derivatives.

## Mental Model

```text
forward pass: inputs -> operations -> loss
backward pass: loss gradient -> operation gradients -> parameter gradients
optimizer: parameters <- updated parameters
```

The training loop repeats this process over batches.

## Core Invariant

Every differentiable operation must know how to propagate gradients to the values it depends on.

## Tiny Example

If `z = x * y`, then a gradient arriving at `z` contributes `grad_z * y` to `x` and `grad_z * x` to `y`.

## Common Misconceptions

- Autograd is not magic; every operation needs a derivative rule.
- Training and inference have different resource profiles.
- Batching changes throughput and latency tradeoffs.
- Model quality and system performance must both be measured.

## Self-Check

1. What graph is built during the forward pass?
2. What values must be saved for backward?
3. Where do gradients accumulate?
4. How does batching affect memory?

## Further Reading

- Stanford CS329S: https://bulletin.stanford.edu/courses/2230771
- CMU Deep Learning Systems course catalog entry: https://coursecatalog.web.cmu.edu/schools-colleges/schoolofcomputerscience/courses/
- Machine Learning in Production at CMU: https://mlip-cmu.github.io/

