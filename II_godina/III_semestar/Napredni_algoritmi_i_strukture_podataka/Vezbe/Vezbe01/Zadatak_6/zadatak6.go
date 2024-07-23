package main

import (
	"fmt"
	"math"
)

func isArmstrong(broj int) bool {
	var copy int = broj
	var sum int = 0
	var digits = make([]int, 0)
	for copy > 0 {
		digits = append(digits, copy%10)
		copy /= 10
	}
	var n int = len(digits)
	for _, digit := range digits {
		sum += int(math.Pow(float64(digit), float64(n)))
	}
	return sum == broj
}

func main() {
	broj := 154
	if isArmstrong(broj) {
		fmt.Println("Broj", broj, "je Armstrongov broj.")
	} else {
		fmt.Println("Broj", broj, "nije Armstrongov broj.")
	}
}
