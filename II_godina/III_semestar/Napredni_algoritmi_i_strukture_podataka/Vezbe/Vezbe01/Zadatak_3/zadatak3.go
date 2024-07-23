package main

import "fmt"

func isPrime(n int32) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	for i := int32(3); i*i <= n; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

type primeIndexError struct {
	n int32
}

func (e *primeIndexError) Error() string {
	return fmt.Sprintf("Ne postoji %d. prost broj", e.n)
}

func nthPrime(n int32) (int32, error) {
	if n < 1 {
		return 0, &primeIndexError{n}
	}
	count := int32(0)
	for i := int32(2); ; i++ {
		if isPrime(i) {
			count++
			if count == n {
				return i, nil
			}
		}
	}
}

func main() {
	n := int32(1)
	prime, err := nthPrime(n)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("%d. prost broj: %d\n", n, prime)
}
