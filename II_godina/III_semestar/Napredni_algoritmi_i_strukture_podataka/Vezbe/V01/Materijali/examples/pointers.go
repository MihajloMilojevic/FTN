package main

import "fmt"

func main() {
	i := 5
	var p *int = &i // u pokaziva£ p upisuje se adresa
	// memorijske lokacije na kojoj se nalazi i
	fmt.Println(p)
	// output: 0xc00000a098 (neka adresa)
	fmt.Println(*p)
	// output: 5
	*p += 5
	fmt.Println(*p)
	//output: 10
}
