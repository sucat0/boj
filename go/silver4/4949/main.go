package main

import (
	"bufio"
	"os"
)

var (
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()
	for {
		lineBytes, _, _ := reader.ReadLine()
		line := string(lineBytes)

		// EOF
		if line == "." {
			break
		}

		stack := make([]rune, 0)
		stackTop := -1
		isBalanced := true
		for _, c := range line {
			switch c {
			case '(':
				stack = append(stack, c)
				stackTop++

			case ')':
				if stackTop == -1 {
					isBalanced = false
					break
				}

				if stack[stackTop] == '(' {
					stack = stack[:stackTop]
					stackTop--
				} else {
					isBalanced = false
					break
				}

			case '[':
				stack = append(stack, c)
				stackTop++

			case ']':
				if stackTop == -1 {
					isBalanced = false
					break
				}

				if stack[stackTop] == '[' {
					stack = stack[:stackTop]
					stackTop--
				} else {
					isBalanced = false
					break
				}
			}
		}

		if isBalanced && stackTop == -1 {
			writer.WriteString("yes\n")
		} else {
			writer.WriteString("no\n")
		}
	}
}
