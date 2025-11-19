package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func main() {
	var (
	v1 = Vertex{1, 2}
	v2 = Vertex{X: 1}
	v3 = Vertex{}
	p *Vertex = &Vertex{1, 2}
	)
	fmt.Println(v1, p.Y, v2, v3)
	//output: {1 2} 2 {1 0} {0 0}

	v := Vertex{3, 4}
	fmt.Println(v.Abs())
	//output: 5
	v.Scale(10)
	fmt.Println(v.Abs())
	//output: 50
}
