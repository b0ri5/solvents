package p01

import "testing"

func TestFortytwo(t *testing.T) {
	if x := fortytwo(); x != 42 {
		t.Errorf("Expected 42 but was %v", x)
	}
}
