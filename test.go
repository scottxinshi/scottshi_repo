package main

import (
	"fmt"
)

func main() {
	const name, age = "Scott", 30
	// fmt.Printf("%s is %d yrs old\n", name, age)
	fmt.Printf("%s is %d yrs old\n the type is %T and the type is %T", name, age, name, age)

	x, y := "happily", 65
	fmt.Printf("\npeople will retire %s at %d", x, y)

	var z int
	fmt.Println("the value is: ", z)
	// the init value of int is 0

	var m int = 100
	fmt.Println("the value is:", m)
	fmt.Printf(" 100 as binary : %b", m)
	fmt.Printf(" 100 as hexadecimal : %x \n", m)

	a, b, c, d := 0, 1, 2, 42
	fmt.Printf("%v \t %b \t %x \n", a, a, a)
	fmt.Printf("%v \t %b \t %x \n", b, b, b)
	fmt.Printf("%v \t %b \t %x \n", c, c, c)
	fmt.Printf("%v \t %b \t %x \n", d, d, d)
}
