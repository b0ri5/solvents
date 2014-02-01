package p0001

func bruteForce(n int) int {
	sum := 0
	for i := 0; i < n; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}
	return sum
}

func linearSum(k int) int {
	return k * (k + 1) / 2
}

func closedForm(n int) int {
	m := n - 1
	return 3*linearSum(m/3) +
		5*linearSum(m/5) -
		15*linearSum(m/15)
}

func goroutineWithChannel(n int) int {
	divisors := make(chan int)
	go func() {
		defer close(divisors)
		for i := 0; i < n; i++ {
			if i%3 == 0 || i%5 == 0 {
				divisors <- i
			}
		}
	}()

	sum := 0
	for i := range divisors {
		sum += i
	}
	return sum
}

func bufferedChannel(n int) int {
	divisors := make(chan int, n)
	for i := 0; i < n; i++ {
		if i%3 == 0 || i%5 == 0 {
			divisors <- i
		}
	}
	close(divisors)

	sum := 0
	for i := range divisors {
		sum += i
	}
	return sum
}
