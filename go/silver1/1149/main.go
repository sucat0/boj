package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
)

var (
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
	dp     = make([]int, 3)
)

func main() {
	defer writer.Flush()

	nBytes, _, _ := reader.ReadLine()
	n, _ := strconv.Atoi(string(nBytes))

	for i := 0; i < n; i++ {
		priceBytes, _, _ := reader.ReadLine()
		prices := strings.Split(string(priceBytes), " ")
		R, _ := strconv.Atoi(prices[0])
		G, _ := strconv.Atoi(prices[1])
		B, _ := strconv.Atoi(prices[2])

		if i == 0 {
			dp[0], dp[1], dp[2] = R, G, B
			continue
		}

		dpBuffer := [3]int{dp[0], dp[1], dp[2]}
		if dpBuffer[1] > dpBuffer[2] {
			dp[0] = dpBuffer[2] + R
		} else {
			dp[0] = dpBuffer[1] + R
		}

		if dpBuffer[0] > dpBuffer[2] {
			dp[1] = dpBuffer[2] + G
		} else {
			dp[1] = dpBuffer[0] + G
		}

		if dpBuffer[0] > dpBuffer[1] {
			dp[2] = dpBuffer[1] + B
		} else {
			dp[2] = dpBuffer[0] + B
		}
	}

	sort.Ints(dp)

	writer.WriteString(strconv.Itoa(dp[0]))
}
