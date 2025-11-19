package main

import (
	"fmt"
	"os"
	)

func main() {
	fmt.Println("Hello World")
	file, err := os.OpenFile("./data/f1.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0755)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	buffer := make([]byte, 1024)
	fmt.Println("File opened successfully")
	n, err := file.Read(buffer)
	if err != nil {
		panic(err)
	}
	fmt.Println("Read ", n, " bytes")
	fmt.Println("Data read: ", string(buffer[:n]))
	file.Write([]byte("Hello World\n"))
}
