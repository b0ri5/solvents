package p0001

import (
	"reflect"
	"runtime"
	"testing"
)

func functionName(f interface{}) string {
	return runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
}

func TestSolutions(t *testing.T) {
	solutions := []func(int) int{
		bruteForce,
		bufferedChannel,
		closedForm,
		goroutineWithChannel,
	}
	cases := []struct {
		n        int
		expected int
	}{
		{3, 0},
		{4, 3},
		{5, 3},
		{6, 8},
		{10, 23},
		{1000, 233168},
	}
	for _, solution := range solutions {
		for _, c := range cases {
			if x := solution(c.n); x != c.expected {
				t.Errorf("For %s expected %d but was %d", functionName(solution), c.expected, x)
			}
		}
	}

}
