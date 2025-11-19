package main

import (
	"crypto/md5"
	"fmt"
)

func GetHashAsString(data []byte) string {
	hash := md5.Sum(data)
	res := ""
	for _, b := range hash {
		res = fmt.Sprintf("%s%b", res, b)
	}
	return res
}

func main() {
	fmt.Println(GetHashAsString([]byte("hello world!")))
}
