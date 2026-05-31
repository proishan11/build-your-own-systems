package page

import "errors"

var (
	ErrNoSpace        = errors.New("page: no space")
	ErrNotFound       = errors.New("page: slot not found")
	ErrNotImplemented = errors.New("page: not implemented")
)

type SlotID int

type Page struct {
	size int
}

func New(size int) *Page {
	return &Page{size: size}
}

// Insert stores record bytes and returns a stable slot id.
func (p *Page) Insert(record []byte) (SlotID, error) {
	return 0, ErrNotImplemented
}

// Get returns a copy of the record stored at slot.
func (p *Page) Get(slot SlotID) ([]byte, error) {
	return nil, ErrNotImplemented
}

// Delete marks a slot as deleted.
func (p *Page) Delete(slot SlotID) error {
	return ErrNotImplemented
}

// FreeSpace reports remaining usable bytes.
func (p *Page) FreeSpace() int {
	return 0
}

