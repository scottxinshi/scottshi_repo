package main

import "fmt"

var num1 = 55
var num3 float32
var num4 string
var num5 bool
var num6 float32 = .0888
var num7 bool

const publisher = "XinHua"

var quote = "How old are you \n I am 3 yrs old"

// var firstName, age = "Scott", 25

func main() {

	// type inferred
	firstName, age := "Scott", 25
	// var firstName, age = "Scott", 25

	fmt.Println(num1)
	fmt.Println(num3)
	fmt.Println(num4)
	fmt.Println(num5)
	fmt.Println(num6)

	fmt.Println(firstName)
	fmt.Println(age)
	//
	//

	fmt.Println(publisher)

	fmt.Println(quote)
}
