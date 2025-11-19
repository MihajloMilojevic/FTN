package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	// zasto ovako formiramo putanju do fajla?
	filePath := fmt.Sprintf("files%cfile.txt", os.PathSeparator)
	// u otvoreni fajl mozemo pisati i mozemo citati njegov sadrzaj
	// ako fajl na navedenoj putanji ne postoji, bice implicitno kreiran
	file, err := os.OpenFile(filePath, os.O_RDWR|os.O_CREATE, 0644)
	if err != nil {
		log.Fatalln(err)
	}
	defer file.Close()
	file.Seek(0, 2)

	// funkciji prosledjujemo promenljivu tipa io.Writer koji je interfejs
	// writer ne mora biti samo fajl, moze biti i bafer u memoriji u koji mozemo pisati, socket itd.
	writer := bufio.NewWriter(file)
	// na kojoj poziciji u fajlu ce se upisati sadrzaj?
	_, err = writer.WriteString("some text\n")
	if err != nil {
		log.Fatalln(err)
	}
	// na kojoj poziciji u fajlu ce se upisati sadrzaj?
	_, err = writer.WriteString("some more text\n")
	if err != nil {
		log.Fatalln(err)
	}
	// izmene se perzistiraju na disk, do ovog trenutka su bile prisutne u baferu u memoriji
	writer.Flush()

	file.Seek(0, 0)
	scanner := bufio.NewScanner(file)
	// Scan() metoda cita liniju po liniju teksta
	// vraca true ako imamo jos linija nakon toga, false ako nemamo
	// odakle krecemo da citamo sadrzaj?
	for scanner.Scan() {
		if err := scanner.Err(); err != nil {
			log.Fatalln(err)
		}
		// kako bismo preuzeli sadrzaj koji je Scan() procitala, pozivamo metodu Text()
		fmt.Println(scanner.Text())
	}
}
