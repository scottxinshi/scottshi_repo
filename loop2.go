package main

import (
	"fmt"
)

func main() {
	var OS [3]string
	OS[0] = "iOS"
	OS[1] = "Android"
	OS[2] = "Windows"

	for v, t := range OS {
		fmt.Println(v, t)
		// for i := range OS {
		// 	fmt.Println(i)

	Outerloop:
		for pos, char := range "Hello, World" {
			if pos == 5 {
				break Outerloop
			}
			fmt.Printf("%d %c \n", pos, char)
		}
	}
}
