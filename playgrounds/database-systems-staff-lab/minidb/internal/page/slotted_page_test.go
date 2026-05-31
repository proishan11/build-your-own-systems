package page

import (
	"bytes"
	"errors"
	"testing"
)

func TestInsertAndGet(t *testing.T) {
	p := New(128)

	slot, err := p.Insert([]byte("alpha"))
	if err != nil {
		t.Fatalf("Insert failed: %v", err)
	}

	got, err := p.Get(slot)
	if err != nil {
		t.Fatalf("Get failed: %v", err)
	}
	if !bytes.Equal(got, []byte("alpha")) {
		t.Fatalf("got %q", got)
	}
}

func TestDeleteMakesSlotMissing(t *testing.T) {
	p := New(128)
	slot, err := p.Insert([]byte("alpha"))
	if err != nil {
		t.Fatalf("Insert failed: %v", err)
	}

	if err := p.Delete(slot); err != nil {
		t.Fatalf("Delete failed: %v", err)
	}

	_, err = p.Get(slot)
	if !errors.Is(err, ErrNotFound) {
		t.Fatalf("expected ErrNotFound, got %v", err)
	}
}

func TestReportsNoSpace(t *testing.T) {
	p := New(32)
	_, err := p.Insert(bytes.Repeat([]byte("x"), 128))
	if !errors.Is(err, ErrNoSpace) {
		t.Fatalf("expected ErrNoSpace, got %v", err)
	}
}

