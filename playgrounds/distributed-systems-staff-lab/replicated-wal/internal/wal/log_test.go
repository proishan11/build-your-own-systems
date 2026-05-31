package wal

import (
	"bytes"
	"context"
	"errors"
	"testing"
)

func TestAppendReturnsMonotonicIndexes(t *testing.T) {
	log, err := Open(t.TempDir(), Options{})
	if err != nil {
		t.Fatalf("Open failed: %v", err)
	}
	defer log.Close()

	first, err := log.Append(context.Background(), []byte("alpha"))
	if err != nil {
		t.Fatalf("Append first failed: %v", err)
	}

	second, err := log.Append(context.Background(), []byte("beta"))
	if err != nil {
		t.Fatalf("Append second failed: %v", err)
	}

	if first != 1 || second != 2 {
		t.Fatalf("unexpected indexes: first=%d second=%d", first, second)
	}
}

func TestReadReturnsAppendedPayload(t *testing.T) {
	log, err := Open(t.TempDir(), Options{})
	if err != nil {
		t.Fatalf("Open failed: %v", err)
	}
	defer log.Close()

	index, err := log.Append(context.Background(), []byte("alpha"))
	if err != nil {
		t.Fatalf("Append failed: %v", err)
	}

	got, err := log.Read(index)
	if err != nil {
		t.Fatalf("Read failed: %v", err)
	}

	if !bytes.Equal(got, []byte("alpha")) {
		t.Fatalf("payload mismatch: got %q", got)
	}
}

func TestReadMissingIndex(t *testing.T) {
	log, err := Open(t.TempDir(), Options{})
	if err != nil {
		t.Fatalf("Open failed: %v", err)
	}
	defer log.Close()

	_, err = log.Read(42)
	if !errors.Is(err, ErrNotFound) {
		t.Fatalf("expected ErrNotFound, got %v", err)
	}
}

func TestRecoverAfterReopen(t *testing.T) {
	dir := t.TempDir()

	log, err := Open(dir, Options{Sync: true})
	if err != nil {
		t.Fatalf("Open failed: %v", err)
	}

	index, err := log.Append(context.Background(), []byte("survives restart"))
	if err != nil {
		t.Fatalf("Append failed: %v", err)
	}

	if err := log.Close(); err != nil {
		t.Fatalf("Close failed: %v", err)
	}

	reopened, err := Open(dir, Options{Sync: true})
	if err != nil {
		t.Fatalf("reopen failed: %v", err)
	}
	defer reopened.Close()

	got, err := reopened.Read(index)
	if err != nil {
		t.Fatalf("Read after reopen failed: %v", err)
	}

	if !bytes.Equal(got, []byte("survives restart")) {
		t.Fatalf("payload mismatch after reopen: got %q", got)
	}
}

