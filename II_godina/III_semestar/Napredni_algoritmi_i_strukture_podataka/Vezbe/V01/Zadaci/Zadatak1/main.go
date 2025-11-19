package main

import "fmt"


func main() {
	fmt.Println("Zadatak 1")
	var broj int32
	fmt.Print("Unesi broj: ")
	fmt.Scanf("%d", &broj)
	fmt.Printf("Pomocu if-else\n")
	if (broj > 0) {
		fmt.Printf("Broj %d je veći od 0\n", broj)
	} else if (broj < 0) {
		fmt.Printf("Broj %d je manji od 0\n", broj)
	} else {
		fmt.Printf("Broj %d je jednak 0\n", broj)		
	}
			
	fmt.Printf("Pomocu switch-case\n")
	switch {
		case broj > 0:
			fmt.Printf("Broj %d je veći od 0\n", broj)
		case broj < 0:
			fmt.Printf("Broj %d je manji od 0\n", broj)
		default:
			fmt.Printf("Broj %d je jednal 0\n", broj)
	}
}