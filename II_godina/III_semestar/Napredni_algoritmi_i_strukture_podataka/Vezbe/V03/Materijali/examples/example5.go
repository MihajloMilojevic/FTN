package main

import (
	"encoding/binary"
	"fmt"
	"log"
	"os"
)

type Sport struct {
	Name          string
	IsTeam        bool
	MatchDuration uint16
}

func (s Sport) Serialize() []byte {
	bytes := make([]byte, 2)
	binary.LittleEndian.PutUint16(bytes, uint16(s.MatchDuration))
	if s.IsTeam {
		bytes = append(bytes, byte(1))
	} else {
		bytes = append(bytes, byte(0))
	}
	nameBytes := []byte(s.Name)
	nameLen := len(nameBytes)
	nameLenBytes := make([]byte, 8)
	binary.LittleEndian.PutUint64(nameLenBytes, uint64(nameLen))
	bytes = append(bytes, nameLenBytes...)
	bytes = append(bytes, nameBytes...)
	return bytes
}

func (s *Sport) Deserialize(file *os.File) error {
	durationBytes := make([]byte, 2)
	_, err := file.Read(durationBytes)
	if err != nil {
		return err
	}
	s.MatchDuration = binary.LittleEndian.Uint16(durationBytes)
	isTeamBytes := make([]byte, 1)
	_, err = file.Read(isTeamBytes)
	if err != nil {
		return err
	}
	isTeam := int8(isTeamBytes[0])
	if isTeam == 0 {
		s.IsTeam = false
	} else {
		s.IsTeam = true
	}
	nameLenBytes := make([]byte, 8)
	_, err = file.Read(nameLenBytes)
	if err != nil {
		return err
	}
	nameLen := binary.LittleEndian.Uint64(nameLenBytes)
	nameBytes := make([]byte, nameLen)
	_, err = file.Read(nameBytes)
	if err != nil {
		return err
	}
	s.Name = string(nameBytes)
	return nil
}

func main() {
	filePath := fmt.Sprintf("files%cfile5.bin", os.PathSeparator)
	file, err := os.OpenFile(filePath, os.O_RDWR|os.O_CREATE, 0644)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	Serialize(file)
	Deserialize(file)
}

func Serialize(file *os.File) {
	f := Sport{Name: "football", IsTeam: true, MatchDuration: 90}
	b := Sport{Name: "basketball", IsTeam: true, MatchDuration: 40}
	_, err := file.Write(f.Serialize())
	if err != nil {
		panic(err)
	}
	_, err = file.Write(b.Serialize())
	if err != nil {
		panic(err)
	}
}

func Deserialize(file *os.File) {
	file.Seek(0, 0)
	var err error
	for err == nil {
		s := new(Sport)
		err = s.Deserialize(file)
		if err == nil {
			log.Println(s)
		}
	}
	// log.Println(err)
}
