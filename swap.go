package main

import (
	"fmt"
)

func swap(a, b *int) {
	*a, *b = *b, *a
}

func addNum(num1, num2 int) int {
	return num1 + num2
}

func addNum2(num1, num2 int) (sum int) {
	sum = num1 + num2
	return
}

func countOddEven(s string) (int, int) {
	odds, evens := 0, 0
	for _, c := range s {
		if int(c)%2 == 0 {
			evens++
		} else {
			odds++
		}
	}
	return odds, evens
}

func addNums(nums ...int) int {
	// fmt.Printf("%T", nums)
	total := 0
	for _, n := range nums {
		total += n
	}
	return total
}

func main() {
	x := 5
	y := 6
	swap(&x, &y)
	fmt.Println(x, y)

	s := addNum(5, 6)
	fmt.Println(s)

	s1 := addNum2(9, 7)
	fmt.Println(s1)

	e, _ := countOddEven("1234567")
	fmt.Println(e)

	fmt.Println(addNums(1, 2, 3, 4))
}

// func main() {
// 	s := addNum(5, 6)
// 	fmt.Println(s)
// }
