package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const inFile string = "../Input.txt"

func main() {
	// Open file
	file, err := os.Open(inFile)
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
	// get each level number & check safety
	var safeCount int

	for _, level := range legible {
		// level safety
		safe := true
		// Put the numbers in a slice (without spaces)
		levelNumsStr := strings.Split(level, " ")
		// Convert first number in level & remove from level for analysis
		lastLevelNum, err := strconv.ParseInt(levelNumsStr[0], 10, 32)
		checkErr(err)
		levelNumsStr = levelNumsStr[1:]
		// Flag if level is increasing or decreasing
		direction := 0
		for _, num := range levelNumsStr {
			intNum, err := strconv.ParseInt(num, 10, 32)
			checkErr(err)

			if direction == 0 {
				if intNum <= lastLevelNum+3 && intNum >= lastLevelNum-3 && intNum != lastLevelNum {
					if intNum > lastLevelNum && intNum != lastLevelNum {
						direction = 1
						lastLevelNum = intNum
					} else if intNum < lastLevelNum && intNum != lastLevelNum {
						direction = 0
						lastLevelNum = intNum
					} else {
						safe = false
						break
					}
				} else {
					safe = false
					break
				}
			} else if direction == 1 {
				if intNum <= lastLevelNum+3 && intNum > lastLevelNum && intNum != lastLevelNum {
					lastLevelNum = intNum
					continue
				} else {
					safe = false
					break
				}
			} else if direction == -1 {
				if intNum >= lastLevelNum-3 && intNum < lastLevelNum && intNum != lastLevelNum {
					lastLevelNum = intNum
					continue
				} else {
					safe = false
					break
				}
			}
		}
		if safe {
			safeCount++
		}
	}

	fmt.Printf("Total Safe Reports: %v", safeCount)
	file.Close()
}

func checkErr(err error) {
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
}
