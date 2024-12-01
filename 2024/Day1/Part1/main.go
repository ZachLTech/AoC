package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

const inputSize int = 1000

func main() {
	// Open file
	file, err := os.Open("../Input.txt")
	checkErr(err)
	// Read lines
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	// Assign lines to slice
	var legible []string
	for scanner.Scan() {
		legible = append(legible, scanner.Text())
	}
	fmt.Printf("%v\n", legible)
	// make slice for each side & remove extra spaces
	var left, right []int64

	for _, pair := range legible {
		// Put the numbers in a slice (without spaces)
		pairFormatted := strings.Split(pair, "   ")
		// Convert the slice numbers to int
		num1, err := strconv.ParseInt(pairFormatted[0], 10, 32)
		checkErr(err)
		num2, err := strconv.ParseInt(pairFormatted[1], 10, 32)
		checkErr(err)
		// Add left and right arrays
		left = append(left, num1)
		right = append(right, num2)
	}
	// Sort :) I'm so glad I didn't have to do this manually lol
	slices.Sort(left)
	slices.Sort(right)
	// Get the distance for each pair & add to total
	var total float64

	for i := 0; i < inputSize; i++ {
		// Calculate Distance
		distance := math.Abs(float64(left[i] - right[i]))
		total += distance
		// Prints for debugging
		fmt.Printf("Line: %v - %v\n", left[i], right[i])
		fmt.Printf("Distance: %v\n", distance)
	}

	fmt.Printf("Total: %v", total)
	file.Close()
}

func checkErr(err error) {
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
}
