package main

import "fmt"

type Printer interface {
	Print()
}

type Greeter struct {
	name string
}

func (g Greeter) Print() {
	fmt.Printf("Hi %s!\n", g.name)
}

func main() {
	var greeterPrinter Printer = Greeter{"Bob"}
	greeterPrinter.Print()
	//output: Hi Bob!
}
