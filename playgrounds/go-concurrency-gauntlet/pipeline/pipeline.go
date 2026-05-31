package pipeline

import (
	"context"
	"errors"
)

var ErrInvalidWorkerCount = errors.New("workers must be greater than zero")

type Result[T any] struct {
	Value T
	Err   error
}

// Map applies fn to every item received from in using a fixed number of workers.
//
// Implement this as a cancellable fan-out/fan-in pipeline:
//   - validate the worker count
//   - start worker goroutines
//   - have workers stop on ctx cancellation or input close
//   - send Result values without blocking forever when ctx is canceled
//   - close the output channel after all workers have exited
//
// Keep the API honest: cancellation means the caller may receive fewer results
// than inputs if work was not completed or could not be delivered.
func Map[T any, R any](
	ctx context.Context,
	workers int,
	in <-chan T,
	fn func(context.Context, T) (R, error),
) (<-chan Result[R], error) {
	if workers <= 0 {
		return nil, ErrInvalidWorkerCount
	}

	out := make(chan Result[R])

	// TODO: Replace this placeholder with the real worker implementation.
	// The current behavior compiles but does not process any input. The tests
	// in pipeline_test.go define the contract you need to satisfy.
	close(out)
	return out, nil
}

