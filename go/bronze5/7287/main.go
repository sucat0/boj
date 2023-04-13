package main

import (
	"bufio"
	"os"
)

var (
	writer = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()

	writer.WriteString("131\n")
	writer.WriteString("krome\n")
}
