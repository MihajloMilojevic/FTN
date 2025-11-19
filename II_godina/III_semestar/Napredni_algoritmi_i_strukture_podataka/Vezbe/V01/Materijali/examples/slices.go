package main

import "fmt"

var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

func main() {
	a := make([]int, 5, 5)
	printSlice("a", a)
	//output: a len=5 cap=5 [0 0 0 0 0]

	b := make([]int, 0, 5)
	printSlice("b", b)
	//output: b len=0 cap=5 []

	c := b[:2]
	printSlice("c", c)
	//output: c len=2 cap=5 [0 0]

	d := c[2:5]
	printSlice("d", d)
	//output: d len=3 cap=3 [0 0 0]

	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}
	// output:
	// 2**0 = 1
	// 2**1 = 2
	// ...
}

func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n", s, len(x), cap(x), x)
}
