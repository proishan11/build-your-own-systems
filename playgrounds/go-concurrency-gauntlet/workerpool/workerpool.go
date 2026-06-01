package workerpool

import (
	"context"
	"errors"
	"fmt"
	"sync"
)

var (
	ErrInvalidConfig  = errors.New("workerpool: workers and queue size must be greater than zero")
	ErrShutdown       = errors.New("workerpool: shut down")
	ErrNotImplemented = errors.New("workerpool: not implemented")
)

type Pool[T any] struct {
	workers int
	queue   int

	ctx    context.Context
	cancel context.CancelFunc

	mu           sync.Mutex
	notEmpty     *sync.Cond
	notFull      *sync.Cond
	jobs         []*task[T]
	shuttingDown bool

	workersWg sync.WaitGroup
	jobsWg    sync.WaitGroup
}

type Future[T any] struct {
	done   chan struct{}
	result result[T]
}

type task[T any] struct {
	run    func(context.Context) (T, error)
	future *Future[T]
}

type result[T any] struct {
	value T
	err   error
}

func New[T any](workers int, queue int) (*Pool[T], error) {
	if workers <= 0 || queue <= 0 {
		return nil, ErrInvalidConfig
	}

	ctx, cancel := context.WithCancel(context.Background())
	pool := &Pool[T]{
		workers: workers,
		queue:   queue,
		ctx:     ctx,
		cancel:  cancel,
	}
	pool.notEmpty = sync.NewCond(&pool.mu)
	pool.notFull = sync.NewCond(&pool.mu)

	pool.workersWg.Add(workers)
	for i := 0; i < workers; i++ {
		go pool.worker()
	}

	return pool, nil
}

// Submit accepts a job for execution and returns a future for its result.
//
// Submit blocks while the bounded queue is full. If ctx is canceled before the
// job is accepted, it returns ctx.Err(). If shutdown has begun, it returns
// ErrShutdown.
func (p *Pool[T]) Submit(ctx context.Context, job func(context.Context) (T, error)) (*Future[T], error) {
	if ctx == nil {
		ctx = context.Background()
	}

	future := &Future[T]{done: make(chan struct{})}
	work := &task[T]{run: job, future: future}

	wakeDone := make(chan struct{})
	go func() {
		select {
		case <-ctx.Done():
			p.mu.Lock()
			p.notFull.Broadcast()
			p.mu.Unlock()
		case <-wakeDone:
		}
	}()
	defer close(wakeDone)

	p.mu.Lock()
	defer p.mu.Unlock()

	for len(p.jobs) >= p.queue && !p.shuttingDown {
		if err := ctx.Err(); err != nil {
			return nil, err
		}
		p.notFull.Wait()
	}

	if err := ctx.Err(); err != nil {
		return nil, err
	}
	if p.shuttingDown {
		return nil, ErrShutdown
	}

	p.jobsWg.Add(1)
	p.jobs = append(p.jobs, work)
	p.notEmpty.Signal()
	return future, nil
}

// Result waits for the job to finish or ctx to be canceled.
func (f *Future[T]) Result(ctx context.Context) (T, error) {
	if ctx == nil {
		ctx = context.Background()
	}

	select {
	case <-f.done:
		return f.result.value, f.result.err
	default:
	}

	select {
	case <-f.done:
		return f.result.value, f.result.err
	case <-ctx.Done():
		var zero T
		return zero, ctx.Err()
	}
}

// Shutdown stops accepting jobs and waits for accepted jobs to complete.
func (p *Pool[T]) Shutdown(ctx context.Context) error {
	if ctx == nil {
		ctx = context.Background()
	}

	p.mu.Lock()
	if !p.shuttingDown {
		p.shuttingDown = true
		p.cancel()
		p.notEmpty.Broadcast()
		p.notFull.Broadcast()
	}
	p.mu.Unlock()

	done := make(chan struct{})
	go func() {
		p.jobsWg.Wait()
		p.workersWg.Wait()
		close(done)
	}()

	select {
	case <-done:
		return nil
	default:
	}

	select {
	case <-done:
		return nil
	case <-ctx.Done():
		return ctx.Err()
	}
}

func (p *Pool[T]) worker() {
	defer p.workersWg.Done()

	for {
		p.mu.Lock()
		for len(p.jobs) == 0 && !p.shuttingDown {
			p.notEmpty.Wait()
		}
		if len(p.jobs) == 0 && p.shuttingDown {
			p.mu.Unlock()
			return
		}
		work := p.jobs[0]
		copy(p.jobs, p.jobs[1:])
		p.jobs[len(p.jobs)-1] = nil
		p.jobs = p.jobs[:len(p.jobs)-1]
		p.notFull.Signal()
		p.mu.Unlock()

		p.run(work)
	}
}

func (p *Pool[T]) run(work *task[T]) {
	defer p.jobsWg.Done()

	var zero T
	value := zero
	var err error

	defer func() {
		if recovered := recover(); recovered != nil {
			value = zero
			err = fmt.Errorf("workerpool: job panic: %v", recovered)
		}
		work.future.complete(value, err)
	}()

	value, err = work.run(p.ctx)
}

func (f *Future[T]) complete(value T, err error) {
	f.result = result[T]{value: value, err: err}
	close(f.done)
}
