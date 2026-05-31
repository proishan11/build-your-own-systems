package btree

import (
	"errors"
	"reflect"
	"testing"
)

func TestInsertAndGet(t *testing.T) {
	tree, err := New(3)
	if err != nil {
		t.Fatalf("New failed: %v", err)
	}

	if err := tree.Insert(10, "ten"); err != nil {
		t.Fatalf("Insert failed: %v", err)
	}
	got, err := tree.Get(10)
	if err != nil {
		t.Fatalf("Get failed: %v", err)
	}
	if got != "ten" {
		t.Fatalf("got %q", got)
	}
}

func TestInsertOverwrites(t *testing.T) {
	tree, _ := New(3)
	if err := tree.Insert(10, "ten"); err != nil {
		t.Fatalf("Insert failed: %v", err)
	}
	if err := tree.Insert(10, "TEN"); err != nil {
		t.Fatalf("overwrite failed: %v", err)
	}
	got, err := tree.Get(10)
	if err != nil {
		t.Fatalf("Get failed: %v", err)
	}
	if got != "TEN" {
		t.Fatalf("got %q", got)
	}
}

func TestMissingKey(t *testing.T) {
	tree, _ := New(3)
	_, err := tree.Get(99)
	if !errors.Is(err, ErrNotFound) {
		t.Fatalf("expected ErrNotFound, got %v", err)
	}
}

func TestRangeReturnsSortedKeys(t *testing.T) {
	tree, _ := New(3)
	for _, key := range []int{5, 1, 3, 2, 4, 9} {
		if err := tree.Insert(key, "x"); err != nil {
			t.Fatalf("Insert %d failed: %v", key, err)
		}
	}
	got, err := tree.Range(2, 5)
	if err != nil {
		t.Fatalf("Range failed: %v", err)
	}
	want := []int{2, 3, 4, 5}
	if !reflect.DeepEqual(got, want) {
		t.Fatalf("got %v want %v", got, want)
	}
}

