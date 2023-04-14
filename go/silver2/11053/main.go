package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

var (
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()

	nByte, _, _ := reader.ReadLine()
	n, _ := strconv.Atoi(string(nByte))

	arrByte, _, _ := reader.ReadLine()
	numStr := strings.Split(string(arrByte), " ")

	arr := make([]int, n)
	for i, num := range numStr {
		arr[i], _ = strconv.Atoi(num)
	}

	dp := make([]int, n)
	max := 1
	for i, num := range arr {
		dp[i] = 1

		if i == 0 {
			continue
		}

		for j := 0; j < i; j++ {
			if num > arr[j] {
				if dp[i] < dp[j]+1 {
					dp[i] = dp[j] + 1

					if max < dp[i] {
						max = dp[i]
					}
				}
			}
		}
	}

	writer.WriteString(strconv.Itoa(max))
}
