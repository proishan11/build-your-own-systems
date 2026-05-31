package queue

import (
	"context"
	"errors"
	"testing"
	"time"
)

func TestRejectsInvalidCapacity(t *testing.T) {
	_, err := New[int](0)
	if !errors.Is(err, ErrInvalidCapacity) {
		t.Fatalf("expected ErrInvalidCapacity, got %v", err)
	}
}

func TestPushPopFIFO(t *testing.T) {
	q, err := New[int](2)
	if err != nil {
		t.Fatalf("New failed: %v", err)
	}

	if err := q.Push(context.Background(), 1); err != nil {
		t.Fatalf("Push 1 failed: %v", err)
	}
	if err := q.Push(context.Background(), 2); err != nil {
		t.Fatalf("Push 2 failed: %v", err)
	}

	first, err := q.Pop(context.Background())
	if err != nil {
		t.Fatalf("Pop first failed: %v", err)
	}
	second, err := q.Pop(context.Background())
	if err != nil {
		t.Fatalf("Pop second failed: %v", err)
	}
	if first != 1 || second != 2 {
		t.Fatalf("not FIFO: got %d then %d", first, second)
	}
}

func TestPushBlocksWhenFullAndUnblocksOnContextCancel(t *testing.T) {
	q, err := New[int](1)
	if err != nil {
		t.Fatalf("New failed: %v", err)
	}
	if err := q.Push(context.Background(), 1); err != nil {
		t.Fatalf("initial Push failed: %v", err)
	}

	ctx, cancel := context.WithTimeout(context.Background(), 25*time.Millisecond)
	defer cancel()

	err = q.Push(ctx, 2)
	if !errors.Is(err, context.DeadlineExceeded) {
		t.Fatalf("expected context deadline, got %v", err)
	}
}

func TestCloseDrainsThenReportsClosed(t *testing.T) {
	q, err := New[string](2)
	if err != nil {
		t.Fatalf("New failed: %v", err)
	}
	if err := q.Push(context.Background(), "a"); err != nil {
		t.Fatalf("Push failed: %v", err)
	}
	if err := q.Close(); err != nil {
		t.Fatalf("Close failed: %v", err)
	}

	got, err := q.Pop(context.Background())
	if err != nil {
		t.Fatalf("expected drain item, got err %v", err)
	}
	if got != "a" {
		t.Fatalf("drain mismatch: got %q", got)
	}

	_, err = q.Pop(context.Background())
	if !errors.Is(err, ErrClosed) {
		t.Fatalf("expected ErrClosed after drain, got %v", err)
	}

	err = q.Push(context.Background(), "b")
	if !errors.Is(err, ErrClosed) {
		t.Fatalf("expected ErrClosed on push after close, got %v", err)
	}
}

