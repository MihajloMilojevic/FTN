package main

import "maps"

func anagrams(word string, candidates []string) []string {
	list := make([]string, 0)
	freq := make(map[rune]int)
	for _, c := range word {
		freq[c]++
	}
	for _, candidate := range candidates {
		if len(candidate) != len(word) {
			continue
		}
		freqCopy := make(map[rune]int)
		maps.Copy(freqCopy, freq)
		isValid := true
		for _, c := range candidate {
			if freqCopy[c] <= 0 {
				isValid = false
				break
			}
			freqCopy[c]--
		}
		if !isValid {
			continue
		}
		for _, v := range freqCopy {
			if v != 0 {
				isValid = false
				break
			}
		}
		if isValid {
			list = append(list, candidate)
		}
	}
	return list
}

func main() {
	word := "listen"
	candidates := []string{"enlists", "google", "inlets", "banana"}
	anagrams := anagrams(word, candidates)
	for _, anagram := range anagrams {
		println(anagram)
	}
}