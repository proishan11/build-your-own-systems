package wal

import (
	"errors"
	"io"
)

var (
	ErrNotImplemented = errors.New("wal: not implemented")
	ErrCorruptRecord  = errors.New("wal: corrupt record")
)

type RecordType uint8

const (
	RecordTypePut RecordType = 1
)

type Record struct {
	LSN     uint64
	Type    RecordType
	Payload []byte
}

// Encode writes one complete WAL record to w.
//
// TODO: Encode a binary record with:
//   - magic bytes
//   - format version
//   - record type
//   - LSN
//   - payload length
//   - payload
//   - checksum
func Encode(w io.Writer, record Record) error {
	return ErrNotImplemented
}

type Scanner struct {
	r      io.Reader
	record Record
	err    error
}

func NewScanner(r io.Reader) *Scanner {
	return &Scanner{r: r}
}

// Next advances to the next complete record.
//
// TODO: Return false without error for a partial final record, because crash
// recovery should ignore a torn tail. Return ErrCorruptRecord for checksum or
// format corruption in a complete record.
func (s *Scanner) Next() bool {
	s.err = ErrNotImplemented
	return false
}

func (s *Scanner) Record() Record {
	return s.record
}

func (s *Scanner) Err() error {
	return s.err
}

