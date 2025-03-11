package main

import (
	"fmt"
)

func main() {
	s := make([]int, 2, 5)

	fmt.Println(s)
	fmt.Println(len(s))
	fmt.Println(cap(s))

	s = append(s, 6, 7, 8, 9)

	fmt.Println(s)
	fmt.Println(len(s))
	fmt.Println(cap(s))
	fmt.Println(s[:5])
	fmt.Println(s[1:])

	t := make([]int, 4, 8)
	for i, v := range t {
		fmt.Println(i, v)
	}
}
