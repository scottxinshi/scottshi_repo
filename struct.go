package main

import (
	"fmt"
)

func main() {

	x := 10
	ptr := &x

	fmt.Println("value of x:", x)
	fmt.Println("Pointer ptr:", ptr)
	fmt.Println("value via ptr:", *ptr)

	*ptr = 20
	fmt.Println("updated value of x:", x)
}
