package pipeline

import (
	"context"
	"errors"
	"reflect"
	"sort"
	"testing"
	"time"
)

func TestMapRejectsInvalidWorkerCount(t *testing.T) {
	in := make(chan int)
	defer close(in)

	_, err := Map(context.Background(), 0, in, func(context.Context, int) (int, error) {
		return 0, nil
	})
	if !errors.Is(err, ErrInvalidWorkerCount) {
		t.Fatalf("expected ErrInvalidWorkerCount, got %v", err)
	}
}

func TestMapProcessesAllInputs(t *testing.T) {
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	in := make(chan int)
	out, err := Map(ctx, 3, in, func(_ context.Context, n int) (int, error) {
		return n * n, nil
	})
	if err != nil {
		t.Fatalf("Map returned error: %v", err)
	}

	go func() {
		defer close(in)
		for i := 1; i <= 5; i++ {
			in <- i
		}
	}()

	var got []int
	for result := range out {
		if result.Err != nil {
			t.Fatalf("unexpected worker error: %v", result.Err)
		}
		got = append(got, result.Value)
	}

	sort.Ints(got)
	want := []int{1, 4, 9, 16, 25}
	if !reflect.DeepEqual(got, want) {
		t.Fatalf("results mismatch\ngot:  %v\nwant: %v", got, want)
	}
}

func TestMapPropagatesWorkerErrors(t *testing.T) {
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	in := make(chan int)
	expected := errors.New("boom")

	out, err := Map(ctx, 2, in, func(_ context.Context, n int) (int, error) {
		if n == 2 {
			return 0, expected
		}
		return n, nil
	})
	if err != nil {
		t.Fatalf("Map returned error: %v", err)
	}

	go func() {
		defer close(in)
		in <- 1
		in <- 2
	}()

	var sawErr bool
	for result := range out {
		if errors.Is(result.Err, expected) {
			sawErr = true
		}
	}

	if !sawErr {
		t.Fatal("expected worker error to be emitted")
	}
}

func TestMapStopsAfterCancellationWhenDownstreamStopsReading(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	in := make(chan int, 10)

	out, err := Map(ctx, 4, in, func(ctx context.Context, n int) (int, error) {
		select {
		case <-ctx.Done():
			return 0, ctx.Err()
		default:
			return n, nil
		}
	})
	if err != nil {
		t.Fatalf("Map returned error: %v", err)
	}

	for i := 0; i < 10; i++ {
		in <- i
	}

	cancel()

	select {
	case <-out:
		// It is okay if one already-computed result was delivered.
	case <-time.After(time.Second):
		t.Fatal("output did not unblock after cancellation")
	}

	select {
	case _, ok := <-out:
		if ok {
			for range out {
			}
		}
	case <-time.After(time.Second):
		t.Fatal("output channel was not closed after cancellation")
	}
}
