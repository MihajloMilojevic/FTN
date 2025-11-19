package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	filePath := fmt.Sprintf("files%cfile3.bin", os.PathSeparator)
	file, err := os.OpenFile(filePath, os.O_RDWR|os.O_CREATE, 0644)
	if err != nil {
		log.Fatalln(err)
	}
	defer file.Close()

	// CITANJE SADRZAJA CELOG FAJLA - 1. NACIN

	// iz FileInfo strukture mozemo procitati duzinu fajla
	info, err := os.Stat(filePath)
	if err != nil {
		log.Fatalln(err)
	}

	writer := bufio.NewWriter(file)
	reader := bufio.NewReader(file)

	data := make([]byte, info.Size())
	// u niz bajtova upisujemo sadrzaj fajla od trenutne pozicije dok ne popunimo niz
	// nakon toga, trenutna pozicija u fajlu pomera se na poslednji procitani bajt
	_, err = reader.Read(data)
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(data)

	// CITANJE SADRZAJA CELOG FAJLA - 2. NACIN

	data2 := make([]byte, 0)
	file.Seek(0, 0)
	b, err := reader.ReadByte()
	for err == nil {
		data2 = append(data2, b)
		b, err = reader.ReadByte()
	}
	log.Println(data2)

	// ZAPIS U FAJL
	// file.Seek(0, 0)
	_, err = writer.Write(
		[]byte{65, 66, 67},
	)
	writer.Flush()
}
