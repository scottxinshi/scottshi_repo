package main

import (
	"fmt"
	"time"
)

// func displayDate() {
// 	fmt.Println(time.Now().Date())

// func main() {
// 	displayDate()
// }
// }

func main() {
	currentTime := time.Now()

	fmt.Println("Current Time in String: ", currentTime.String())
	fmt.Println("MM-DD-YYYY :", currentTime.Format("09-07-2024"))
}

