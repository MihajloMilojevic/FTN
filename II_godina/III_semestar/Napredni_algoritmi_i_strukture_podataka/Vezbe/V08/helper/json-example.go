package main

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
)

type Config struct {
	WalSize           uint64 `json:"wal_size"`
	MemtableSize      uint64 `json:"memtable_size"`
	MemtableStructure string `json:"memtable_structure"`
}

func main() {
	var config Config
	configData, err := os.ReadFile("config.json")
	if err != nil {
		log.Fatal(err)
	}
	json.Unmarshal(configData, &config)
	fmt.Println(config)
	marshalled, err := json.Marshal(config)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(marshalled))
}
