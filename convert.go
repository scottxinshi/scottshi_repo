package main

import (
	"fmt"
	"strconv"
)

var queue = 5
var name string = "John"
var s = name + ", your queue number is: " + strconv.Itoa(queue)

var num int = 6

func main() {
	var age int

	fmt.Print("Please enter your age:")
	fmt.Scanf("%d", &age)
	fmt.Println("You entered:", age, "yrs old")

	// queue := 5
	// name := "John"
	// s: = name + ", your queue number is: " + queue

	fmt.Println(s)

	fmt.Println("After checking, the result is", num <= 0 || num >= 6)
}
                                                   