package main

import (
	"fmt"
	"strconv"
)

func arr() {
	nums := [...]int{6, 10, 21, 25, 34, 42}
	fmt.Println(nums[1:3])
}

func main() {
	var table [5][6]string
	for row := 0; row < 5; row++ {
		for column := 0; column < 6; column++ {
			table[row][column] =
				strconv.Itoa(row) + ", " +
					strconv.Itoa(column)
		}
	}
	fmt.Println(table)

	t = make([...]int{70, 80, 90})
	for i, v := range t {
		fmt.Println(i, v)
	}
}
