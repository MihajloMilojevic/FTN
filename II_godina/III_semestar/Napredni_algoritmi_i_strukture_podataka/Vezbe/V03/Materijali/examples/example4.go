package main

import (
	"encoding/binary"
	"fmt"
	"os"
)

type Vertex struct {
	X, Y int64
}

func main() {
	b := []byte{1, 2, 3, 4}
	val := binary.LittleEndian.Uint32(b)
	fmt.Printf("Little endian: %b\n", val)
	//output: Little endian: 00000100000000110000001000000001
	val2 := binary.BigEndian.Uint32(b)
	fmt.Printf("Big endian: %b\n", val2)
	//output: Big endian: 00000001000000100000001100000100
	binary.LittleEndian.PutUint32(b, val2)
	fmt.Println(b)
	//output: [4 3 2 1]

	filePath := fmt.Sprintf("files%cfile4.bin", os.PathSeparator)
	file, err := os.OpenFile(filePath, os.O_RDWR|os.O_CREATE, 0644)
	if err != nil {
		panic(err)
	}

	vertex := Vertex{3, 2}
	vertex2 := Vertex{4, 5}
	err = binary.Write(file, binary.LittleEndian, vertex)
	if err != nil {
		panic(err)
	}
	err = binary.Write(file, binary.LittleEndian, vertex2)
	if err != nil {
		panic(err)
	}

	file.Seek(0, 0)
	newv := &Vertex{}
	err = binary.Read(file, binary.LittleEndian, newv)
	if err != nil {
		panic(err)
	}
	fmt.Println(*newv)
	//output: {3 2}
	err = binary.Read(file, binary.LittleEndian, newv)
	if err != nil {
		panic(err)
	}
	fmt.Println(*newv)
	//output: {4 5}

	str := "abcђш"
	strb := []byte(str)
	fmt.Println(strb)
	str2 := string(strb)
	fmt.Println(str2)
}
