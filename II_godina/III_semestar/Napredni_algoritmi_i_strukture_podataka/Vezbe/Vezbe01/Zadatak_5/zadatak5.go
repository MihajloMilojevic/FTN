package main

import "fmt"

type Student struct {
	ime, prezime, index string
}

func (s *Student) SetIndex(index string) {
	s.index = index
}

func main() {
	var me Student = Student{"Mihajlo", "Milojević", "SV57/2023"}
	fmt.Println(me)
	me.SetIndex("SV-57-2023")
	fmt.Println(me)
}