package main

import (
	"fmt"
	"reflect"
	"time"
)

func main() {

	firstName, lastName, age := "Waylon", "Shi", 7
	start := time.Now()

	fmt.Println(firstName)
	fmt.Println(lastName)
	fmt.Println(age)

	fmt.Println(start)
	fmt.Println(reflect.TypeOf(start))
}
