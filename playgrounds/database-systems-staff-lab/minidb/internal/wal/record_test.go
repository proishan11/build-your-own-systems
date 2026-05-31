package wal

import (
	"bytes"
	"errors"
	"testing"
)

func TestEncodeDecodeRoundTrip(t *testing.T) {
	var buf bytes.Buffer

	input := Record{
		LSN:     7,
		Type:    RecordTypePut,
		Payload: []byte("hello wal"),
	}

	if err := Encode(&buf, input); err != nil {
		t.Fatalf("Encode failed: %v", err)
	}

	scanner := NewScanner(bytes.NewReader(buf.Bytes()))
	if !scanner.Next() {
		t.Fatalf("expected one record, err=%v", scanner.Err())
	}

	got := scanner.Record()
	if got.LSN != input.LSN || got.Type != input.Type || !bytes.Equal(got.Payload, input.Payload) {
		t.Fatalf("record mismatch: got %+v want %+v", got, input)
	}

	if scanner.Next() {
		t.Fatal("expected only one record")
	}
	if err := scanner.Err(); err != nil {
		t.Fatalf("unexpected scanner error: %v", err)
	}
}

func TestScannerReadsMultipleRecords(t *testing.T) {
	var buf bytes.Buffer

	records := []Record{
		{LSN: 1, Type: RecordTypePut, Payload: []byte("a")},
		{LSN: 2, Type: RecordTypePut, Payload: []byte("b")},
		{LSN: 3, Type: RecordTypePut, Payload: []byte("c")},
	}

	for _, record := range records {
		if err := Encode(&buf, record); err != nil {
			t.Fatalf("Encode failed: %v", err)
		}
	}

	scanner := NewScanner(bytes.NewReader(buf.Bytes()))
	var got []uint64
	for scanner.Next() {
		got = append(got, scanner.Record().LSN)
	}
	if err := scanner.Err(); err != nil {
		t.Fatalf("unexpected scanner error: %v", err)
	}

	want := []uint64{1, 2, 3}
	if len(got) != len(want) {
		t.Fatalf("LSN count mismatch: got %v want %v", got, want)
	}
	for i := range want {
		if got[i] != want[i] {
			t.Fatalf("LSN mismatch: got %v want %v", got, want)
		}
	}
}

func TestScannerIgnoresPartialFinalRecord(t *testing.T) {
	var buf bytes.Buffer

	if err := Encode(&buf, Record{LSN: 1, Type: RecordTypePut, Payload: []byte("complete")}); err != nil {
		t.Fatalf("Encode failed: %v", err)
	}

	buf.Write([]byte{0x01, 0x02, 0x03})

	scanner := NewScanner(bytes.NewReader(buf.Bytes()))
	if !scanner.Next() {
		t.Fatalf("expected complete first record, err=%v", scanner.Err())
	}
	if scanner.Next() {
		t.Fatal("partial final record should not be returned")
	}
	if err := scanner.Err(); err != nil {
		t.Fatalf("partial final record should not be an error, got %v", err)
	}
}

func TestScannerReportsCorruption(t *testing.T) {
	var buf bytes.Buffer

	if err := Encode(&buf, Record{LSN: 1, Type: RecordTypePut, Payload: []byte("payload")}); err != nil {
		t.Fatalf("Encode failed: %v", err)
	}

	data := buf.Bytes()
	data[len(data)-1] ^= 0xff

	scanner := NewScanner(bytes.NewReader(data))
	if scanner.Next() {
		t.Fatal("corrupt record should not be returned")
	}
	if !errors.Is(scanner.Err(), ErrCorruptRecord) {
		t.Fatalf("expected ErrCorruptRecord, got %v", scanner.Err())
	}
}

