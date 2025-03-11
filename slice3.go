package main

import (
	"errors"
	"fmt"
)

func delete(orig []int, index int) ([]int, error) {
	if index < 0 {
		return nil, errors.New(
			"Index cannot be less than 0")
	}
	if index > len(orig) {
		return nil, errors.New(
			"index cannot exceed the length of the slice")
	}
	// if index == len(orig) {
	// 	// Append directly if inserting at the end
	// 	return append(orig, value), nil
	// }

	orig = append(orig[:index], orig[index+1:]...)
	// orig[index] = value
	return orig, nil

}

func main() {
	// t := []int{1, 2, 3, 4, 5}
	// v := make([]int, 2, 3)

	// copy(v, t)

	// fmt.Println(t)
	// fmt.Println(v)
	t := []int{1, 2, 3, 4, 5}
	t, err := delete(t, 2)
	if err == nil {
		fmt.Println(t)
	} else {
		fmt.Println(err)
	}
}
