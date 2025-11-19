package main

import "fmt"

func main() {
	slice := []int{10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
	var valueLessThenIndex []int
	for i, v := range slice {
		fmt.Printf("Index: %d, Vrednost: %d\n", i, v)
		if v < i {
			valueLessThenIndex = append(valueLessThenIndex, v)
		}
	}
	fmt.Println("Elementi koji su manji od svog indeksa: ", valueLessThenIndex)
}