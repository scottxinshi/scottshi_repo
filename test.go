package main

import (
	"fmt"
)

func main() {
	const name, age = "Scott", 30
	// fmt.Printf("%s is %d yrs old\n", name, age)
	fmt.Printf("%s is %d yrs old\n the type is %T and the type is %T", name, age, name, age)
}
