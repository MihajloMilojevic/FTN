package bloomfilter

import (
	"fmt"
	"os"
)

func TestBloomFilter() {
	var bl BloomFilter = NewBloomFilter(3, 0.01)
	var a []byte = []byte("a")
	var b []byte = []byte("b")
	var c []byte = []byte("c")

	

	fmt.Printf("Nothing inserted\n\n")
	if bl.IsNotIn(a) {
		fmt.Println(string(a), " is not in bloomfilter")
	} else {
		fmt.Println(string(a), " is maybe in bloomfilter")
	}
	if bl.IsNotIn(b) {
		fmt.Println(string(b), " is not in bloomfilter")
	} else {
		fmt.Println(string(b), " is maybe in bloomfilter")
	}
	if bl.IsNotIn(c) {
		fmt.Println(string(c), " is not in bloomfilter")
	} else {
		fmt.Println(string(c), " is maybe in bloomfilter")
	}
	bl.Insert(a)
	fmt.Printf("\n\nA inserted\n\n")
	if bl.IsNotIn(a) {
		fmt.Println(string(a), " is not in bloomfilter")
	} else {
		fmt.Println(string(a), " is maybe in bloomfilter")
	}
	if bl.IsNotIn(b) {
		fmt.Println(string(b), " is not in bloomfilter")
	} else {
		fmt.Println(string(b), " is maybe in bloomfilter")
	}
	if bl.IsNotIn(c) {
		fmt.Println(string(c), " is not in bloomfilter")
	} else {
		fmt.Println(string(c), " is maybe in bloomfilter")
	}
	bl.Insert(b)
	fmt.Printf("\n\nB inserted\n\n")
	if bl.IsNotIn(a) {
		fmt.Println(string(a), " is not in bloomfilter")
	} else {
		fmt.Println(string(a), " is maybe in bloomfilter")
	}
	if bl.IsNotIn(b) {
		fmt.Println(string(b), " is not in bloomfilter")
	} else {
		fmt.Println(string(b), " is maybe in bloomfilter")
	}
	if bl.IsNotIn(c) {
		fmt.Println(string(c), " is not in bloomfilter")
	} else {
		fmt.Println(string(c), " is maybe in bloomfilter")
	}
	bl.Insert(c)

	fmt.Printf("\n\nC inserted \n\n")
	if bl.IsNotIn(a) {
		fmt.Println(string(a), " is not in bloomfilter")
	} else {
		fmt.Println(string(a), " is maybe in bloomfilter")
	}
	if bl.IsNotIn(b) {
		fmt.Println(string(b), " is not in bloomfilter")
	} else {
		fmt.Println(string(b), " is maybe in bloomfilter")
	}
	if bl.IsNotIn(c) {
		fmt.Println(string(c), " is not in bloomfilter")
	} else {
		fmt.Println(string(c), " is maybe in bloomfilter")
	}

	var blBytes []byte = bl.Serialize()
	filePath := "file.bin"
	file, err := os.OpenFile(filePath, os.O_RDWR|os.O_CREATE, 0644)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	file.Write(blBytes)

	file.Seek(0, 0)

	file.Read(blBytes)
	var bl2 BloomFilter
	bl2.Deserialize(blBytes)

	filePath = "file2.bin"
	file, err = os.OpenFile(filePath, os.O_RDWR|os.O_CREATE, 0644)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	file.Write(bl2.Serialize())

	fmt.Printf("\n\nBL2\n\n")
	if bl2.IsNotIn(a) {
		fmt.Println(string(a), " is not in bloomfilter")
	} else {
		fmt.Println(string(a), " is maybe in bloomfilter")
	}
	if bl2.IsNotIn(b) {
		fmt.Println(string(b), " is not in bloomfilter")
	} else {
		fmt.Println(string(b), " is maybe in bloomfilter")
	}
	if bl2.IsNotIn(c) {
		fmt.Println(string(c), " is not in bloomfilter")
	} else {
		fmt.Println(string(c), " is maybe in bloomfilter")
	}
}
