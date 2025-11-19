package main

import (
	"fmt"
	"V02/model"
	"rsc.io/quote/v4" 
)

func main() {
	// Create a new student
	student := model.Student{
		Name: "John Doe",
	}
	// Print the student's name
	fmt.Println(student.Name)
	if false {
		a()
	}
	fmt.Println(quote.Glass())
}

func a() {
	fmt.Println("a")
}