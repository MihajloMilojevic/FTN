package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	filePath := fmt.Sprintf("files%cfile2.bin", os.PathSeparator)
	file, err := os.OpenFile(filePath, os.O_RDWR|os.O_CREATE, 0644)
	if err != nil {
		log.Fatalln(err)
	}
	defer file.Close()

	_, err = file.Write([]byte{1, 2, 3})
	if err != nil {
		log.Fatalln(err)
	}

	data := make([]byte, 3)
	file.Seek(0, 0)
	_, err = file.Read(data)
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(data)

	_, err = file.ReadAt(data, 0)
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(data)

	_, err = file.WriteAt([]byte{5}, 1)
	if err != nil {
		log.Fatalln(err)
	}

	_, err = file.ReadAt(data, 0)
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(data)
}
