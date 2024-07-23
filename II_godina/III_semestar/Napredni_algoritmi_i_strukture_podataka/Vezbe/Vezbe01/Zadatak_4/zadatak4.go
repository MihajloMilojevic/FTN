package main

import "fmt"

func main() {
	mapa := make(map[string]string)
	mapa["36000"] = "Kraljevo"
	mapa["11000"] = "Beograd"
	mapa["21000"] = "Novi Sad"
	mapa["24000"] = "Subotica"
	mapa["18000"] = "Nis"
	mapa["34000"] = "Kragujevac"
	mapa["23000"] = "Zrenjanin"
	mapa["16000"] = "Leskovac"
	mapa["37000"] = "Krusevac"
	mapa["26000"] = "Pancevo"
	mapa["35000"] = "Cacak"
	imenaGradova := make([]string, 0)
	for broj, grad := range mapa {
		imenaGradova = append(imenaGradova, grad)
		fmt.Println(broj, grad)
	}
	fmt.Println(imenaGradova)
}
