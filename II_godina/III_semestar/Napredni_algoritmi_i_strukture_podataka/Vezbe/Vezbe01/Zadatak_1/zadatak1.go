package main

import "fmt"

func main() {
	broj := 5
	fmt.Print("Korišćenje if-else naredbe\n")
	if broj > 0 {
		fmt.Printf("Broj %d je veci od 0\n", broj)
	} else if broj < 0 {
		fmt.Printf("Broj %d je manji od 0\n", broj)
	} else {
		fmt.Printf("Broj %d je jednak 0\n", broj)
	}
	fmt.Print("Korišćenje switch naredbe\n")
	switch {
		case broj > 0:
			fmt.Printf("Broj %d je veci od 0\n", broj)
		case broj < 0:
			fmt.Printf("Broj %d je manji od 0\n", broj)
		default:
			fmt.Printf("Broj %d je jednak 0\n", broj)
	}
}