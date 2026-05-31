package buffer

import (
	"bytes"
	"context"
	"testing"
)

func TestFetchLoadsPage(t *testing.T) {
	pool, err := New(2, func(_ context.Context, id PageID) ([]byte, error) {
		return []byte{byte(id)}, nil
	}, func(context.Context, PageID, []byte) error {
		return nil
	})
	if err != nil {
		t.Fatalf("New failed: %v", err)
	}

	frame, err := pool.Fetch(context.Background(), 7)
	if err != nil {
		t.Fatalf("Fetch failed: %v", err)
	}
	if frame.ID != 7 || !bytes.Equal(frame.Data, []byte{7}) {
		t.Fatalf("unexpected frame: %+v", frame)
	}
}

func TestPinnedPageIsNotEvicted(t *testing.T) {
	pool, err := New(1, func(_ context.Context, id PageID) ([]byte, error) {
		return []byte{byte(id)}, nil
	}, func(context.Context, PageID, []byte) error {
		return nil
	})
	if err != nil {
		t.Fatalf("New failed: %v", err)
	}

	if _, err := pool.Fetch(context.Background(), 1); err != nil {
		t.Fatalf("Fetch 1 failed: %v", err)
	}
	if _, err := pool.Fetch(context.Background(), 2); err != ErrAllPagesPinned {
		t.Fatalf("expected ErrAllPagesPinned, got %v", err)
	}
}

func TestFlushAllFlushesDirtyPages(t *testing.T) {
	var flushed []PageID
	pool, err := New(2, func(_ context.Context, id PageID) ([]byte, error) {
		return []byte{byte(id)}, nil
	}, func(_ context.Context, id PageID, _ []byte) error {
		flushed = append(flushed, id)
		return nil
	})
	if err != nil {
		t.Fatalf("New failed: %v", err)
	}

	if _, err := pool.Fetch(context.Background(), 1); err != nil {
		t.Fatalf("Fetch failed: %v", err)
	}
	if err := pool.MarkDirty(1); err != nil {
		t.Fatalf("MarkDirty failed: %v", err)
	}
	if err := pool.FlushAll(context.Background()); err != nil {
		t.Fatalf("FlushAll failed: %v", err)
	}
	if len(flushed) != 1 || flushed[0] != 1 {
		t.Fatalf("unexpected flushed pages: %v", flushed)
	}
}

