package buffer

import (
	"context"
	"errors"
)

var (
	ErrInvalidCapacity = errors.New("buffer: capacity must be greater than zero")
	ErrAllPagesPinned  = errors.New("buffer: all pages are pinned")
	ErrNotPinned       = errors.New("buffer: page is not pinned")
	ErrNotImplemented  = errors.New("buffer: not implemented")
)

type PageID uint64

type Frame struct {
	ID   PageID
	Data []byte
}

type Loader func(context.Context, PageID) ([]byte, error)
type Flusher func(context.Context, PageID, []byte) error

type Pool struct {
	capacity int
	load     Loader
	flush    Flusher
}

func New(capacity int, load Loader, flush Flusher) (*Pool, error) {
	if capacity <= 0 {
		return nil, ErrInvalidCapacity
	}
	return &Pool{capacity: capacity, load: load, flush: flush}, nil
}

// Fetch pins and returns the requested page, loading or evicting as needed.
func (p *Pool) Fetch(ctx context.Context, id PageID) (*Frame, error) {
	return nil, ErrNotImplemented
}

func (p *Pool) MarkDirty(id PageID) error {
	return ErrNotImplemented
}

func (p *Pool) Unpin(id PageID) error {
	return ErrNotImplemented
}

func (p *Pool) FlushAll(ctx context.Context) error {
	return ErrNotImplemented
}

