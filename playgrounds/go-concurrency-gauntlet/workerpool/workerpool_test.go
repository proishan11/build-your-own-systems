package workerpool

import (
	"context"
	"errors"
	"testing"
	"time"
)

func TestRejectsInvalidConfig(t *testing.T) {
	_, err := New[int](0, 1)
	if !errors.Is(err, ErrInvalidConfig) {
		t.Fatalf("expected ErrInvalidConfig, got %v", err)
	}
}

func TestRunsSubmittedJob(t *testing.T) {
	pool, err := New[int](2, 4)
	if err != nil {
		t.Fatalf("New failed: %v", err)
	}
	defer pool.Shutdown(context.Background())

	future, err := pool.Submit(context.Background(), func(context.Context) (int, error) {
		return 42, nil
	})
	if err != nil {
		t.Fatalf("Submit failed: %v", err)
	}

	got, err := future.Result(context.Background())
	if err != nil {
		t.Fatalf("Result failed: %v", err)
	}
	if got != 42 {
		t.Fatalf("got %d, want 42", got)
	}
}

func TestResultCanBeCanceled(t *testing.T) {
	pool, err := New[int](1, 1)
	if err != nil {
		t.Fatalf("New failed: %v", err)
	}
	defer pool.Shutdown(context.Background())

	future, err := pool.Submit(context.Background(), func(ctx context.Context) (int, error) {
		<-ctx.Done()
		return 0, ctx.Err()
	})
	if err != nil {
		t.Fatalf("Submit failed: %v", err)
	}

	ctx, cancel := context.WithTimeout(context.Background(), 25*time.Millisecond)
	defer cancel()
	_, err = future.Result(ctx)
	if !errors.Is(err, context.DeadlineExceeded) {
		t.Fatalf("expected deadline from Result, got %v", err)
	}
}

func TestShutdownRejectsNewJobs(t *testing.T) {
	pool, err := New[int](1, 1)
	if err != nil {
		t.Fatalf("New failed: %v", err)
	}

	if err := pool.Shutdown(context.Background()); err != nil {
		t.Fatalf("Shutdown failed: %v", err)
	}

	_, err = pool.Submit(context.Background(), func(context.Context) (int, error) {
		return 1, nil
	})
	if !errors.Is(err, ErrShutdown) {
		t.Fatalf("expected ErrShutdown, got %v", err)
	}
}

