package wal

import (
	"context"
	"errors"
)

var (
	ErrNotImplemented = errors.New("wal: not implemented")
	ErrNotFound       = errors.New("wal: index not found")
)

type Options struct {
	// Sync controls whether Append must force data to stable storage before
	// returning. Later exercises will make this more nuanced with group commit.
	Sync bool
}

type Log struct {
	dir  string
	opts Options
}

// Open opens or creates a local durable log rooted at dir.
func Open(dir string, opts Options) (*Log, error) {
	return &Log{dir: dir, opts: opts}, nil
}

// Append writes payload to the log and returns its monotonically increasing index.
//
// TODO: Implement the local durability boundary:
//   - encode a record
//   - append it to the log file
//   - optionally sync
//   - update the in-memory index only after the write succeeds
func (l *Log) Append(ctx context.Context, payload []byte) (uint64, error) {
	return 0, ErrNotImplemented
}

// Read returns a copy of the payload stored at index.
//
// TODO: Use the in-memory index rebuilt by Open to seek to the record and decode
// it. Return ErrNotFound when index does not exist.
func (l *Log) Read(index uint64) ([]byte, error) {
	return nil, ErrNotImplemented
}

// Close releases files held by the log.
func (l *Log) Close() error {
	return nil
}

