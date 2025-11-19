package main

import (
	"fmt"
	"math/rand"
)

type SkipList struct {
	maxHeight int
}

func (s *SkipList) roll() int {
	level := 0
	// possible ret values from rand are 0 and 1
	// we stop shen we get a 0
	for ; rand.Int31n(2) == 1; level++ {
		if level >= s.maxHeight {
			return level
		}
	}
	return level
}

func main() {
	s := SkipList{maxHeight: 3}
	for i := 0; i < 10; i++ {
		fmt.Println(s.roll())
	}
}
