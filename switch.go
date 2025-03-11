package main

import (
	"fmt"
)

func main() {

	num := 2
	dayOfWeek := " "

	switch num {

	case 1:
		dayOfWeek = "Monday"
		fmt.Println(dayOfWeek)
	case 2:
		dayOfWeek = "Tuesday"
		fmt.Println(dayOfWeek)
	case 3:
		dayOfWeek = "Wednesday"
		fmt.Println(dayOfWeek)
	case 4:
		dayOfWeek = "Thursday"
		fmt.Println(dayOfWeek)
	case 5:
		dayOfWeek = "Friday"
		fmt.Println(dayOfWeek)
	case 6:
		dayOfWeek = "Saturday"
		fmt.Println(dayOfWeek)
	case 7:
		dayOfWeek = "Sunday"
		fmt.Println(dayOfWeek)
	default:
		fmt.Println("--error--")
	}
}
