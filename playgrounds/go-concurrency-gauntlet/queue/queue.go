package queue

import (
	"context"
	"errors"
)

var (
	ErrInvalidCapacity = errors.New("queue: capacity must be greater than zero")
	ErrClosed          = errors.New("queue: closed")
	ErrNotImplemented  = errors.New("queue: not implemented")
)

type Queue[T any] struct {
	capacity int
}

func New[T any](capacity int) (*Queue[T], error) {
	if capacity <= 0 {
		return nil, ErrInvalidCapacity
	}
	return &Queue[T]{capacity: capacity}, nil
}

// Push adds item to the queue, blocking while the queue is full.
//
// TODO: Implement this with explicit synchronization. A correct solution should
// wake waiting consumers when an item arrives and should return promptly when
// ctx is canceled or the queue is closed.
func (q *Queue[T]) Push(ctx context.Context, item T) error {
	return ErrNotImplemented
}

// Pop removes and returns the oldest item, blocking while the queue is empty.
//
// TODO: A closed queue should still allow already-pushed items to drain. Once
// the queue is closed and drained, Pop should return ErrClosed.
func (q *Queue[T]) Pop(ctx context.Context) (T, error) {
	var zero T
	return zero, ErrNotImplemented
}

// Close prevents future pushes and wakes blocked producers and consumers.
func (q *Queue[T]) Close() error {
	return ErrNotImplemented
}

