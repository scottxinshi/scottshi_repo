package main

import (
	"fmt"
)

func main() {
	xi := []int{56, 88, 101, 125}
	for i, v := range xi {
		fmt.Println("ranging over a slice", i, v)
	}

	m := map[string]int{
		"Tom":   8,
		"Jerry": 6,
	}
	for k, v := range m {
		fmt.Println("ranging over a map", k, v)
	}
}
