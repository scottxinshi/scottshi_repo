package main

import (
	"fmt"
	"time"
)

func displayDate(format string, prefix string) {
	fmt.Println(prefix, time.Now().Format(format))

}
func main() {
	displayDate("Mon 2005-01-02", "Current Date and Time:")
	displayDate("2005.01.02 17:06:06", "Current Date and Time:")
}
