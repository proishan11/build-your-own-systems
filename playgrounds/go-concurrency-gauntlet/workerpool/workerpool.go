package workerpool

import (
	"context"
	"errors"
)

var (
	ErrInvalidConfig  = errors.New("workerpool: workers and queue size must be greater than zero")
	ErrShutdown       = errors.New("workerpool: shut down")
	ErrNotImplemented = errors.New("workerpool: not implemented")
)

type Pool[T any] struct {
	workers int
	queue   int
}

type Future[T any] struct{}

func New[T any](workers int, queue int) (*Pool[T], error) {
	if workers <= 0 || queue <= 0 {
		return nil, ErrInvalidConfig
	}
	return &Pool[T]{workers: workers, queue: queue}, nil
}

// Submit accepts a job for execution and returns a future for its result.
//
// TODO: Enqueue jobs into a bounded queue. If ctx is canceled before the job is
// accepted, return ctx.Err(). If shutdown has begun, return ErrShutdown.
func (p *Pool[T]) Submit(ctx context.Context, job func(context.Context) (T, error)) (*Future[T], error) {
	return nil, ErrNotImplemented
}

// Result waits for the job to finish or ctx to be canceled.
func (f *Future[T]) Result(ctx context.Context) (T, error) {
	var zero T
	return zero, ErrNotImplemented
}

// Shutdown stops accepting jobs and waits for accepted jobs to complete.
func (p *Pool[T]) Shutdown(ctx context.Context) error {
	return ErrNotImplemented
}

