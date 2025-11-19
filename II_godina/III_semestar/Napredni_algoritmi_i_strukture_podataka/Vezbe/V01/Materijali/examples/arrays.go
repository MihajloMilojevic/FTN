package main

import "fmt"

func main() {
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	//output: Hello World
	fmt.Println(a)
	//output: [Hello World]	

	nums := [6]int{1, 2, 3, 4}
	fmt.Println(nums)
	//output: 1 2 3 4 0 0
}
