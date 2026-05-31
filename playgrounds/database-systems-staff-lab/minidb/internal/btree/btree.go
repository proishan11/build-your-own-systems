package btree

import "errors"

var (
	ErrInvalidOrder   = errors.New("btree: order must be at least 3")
	ErrNotFound       = errors.New("btree: key not found")
	ErrNotImplemented = errors.New("btree: not implemented")
)

type Tree struct {
	order int
}

func New(order int) (*Tree, error) {
	if order < 3 {
		return nil, ErrInvalidOrder
	}
	return &Tree{order: order}, nil
}

func (t *Tree) Insert(key int, value string) error {
	return ErrNotImplemented
}

func (t *Tree) Get(key int) (string, error) {
	return "", ErrNotImplemented
}

func (t *Tree) Range(start int, end int) ([]int, error) {
	return nil, ErrNotImplemented
}

