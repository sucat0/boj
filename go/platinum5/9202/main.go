// 9202 - Boggle
package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

var (
	reader   = bufio.NewReader(os.Stdin)
	writer   = bufio.NewWriter(os.Stdout)
	wordTrie = newTrie()
	board    = make([][]rune, 4)
)

type trieNode struct {
	child map[rune]*trieNode
	isEnd bool
}

type trie struct {
	root *trieNode
}

func newTrie() *trie {
	return &trie{root: &trieNode{}}
}

func (t *trie) insert(word string) {
	node := t.root

	for _, d := range word {
		if node.child == nil {
			node.child = make(map[rune]*trieNode)
		}

		if node.child[d] == nil {
			node.child[d] = &trieNode{}
		}

		node = node.child[d]
	}

	node.isEnd = true
}

func byteToInt(b []byte) int {
	var i int
	for _, c := range b {
		i *= 10
		i += int(c - '0')
	}

	return i
}

type location struct {
	x, y int
}

func dfs(loc location, visited [][]bool, currentNode *trieNode, currentWord []rune, wordResult map[string]struct{}) {
	c := board[loc.y][loc.x]

	// If there is no word in trie starts with currentNode + c
	if currentNode.child[c] == nil {
		return
	}

	// If currentNode + c is a word
	if currentNode.child[c].isEnd {
		wordResult[string(append(currentWord, c))] = struct{}{}
	}

	// Mark visit
	visited[loc.y][loc.x] = true

	for i := -1; i <= 1; i++ {
		for j := -1; j <= 1; j++ {
			x, y := loc.x+i, loc.y+j

			// Check if x, y is not valid and not visited
			if x < 0 || x >= 4 || y < 0 || y >= 4 || visited[y][x] {
				continue
			}

			// Recursive DFS
			dfs(location{x, y}, visited, currentNode.child[c], append(currentWord, c), wordResult)
		}
	}

	// If returned -> remove visit
	visited[loc.y][loc.x] = false
}

func main() {
	defer writer.Flush()

	// Read words in dictionary
	wBytes, _, _ := reader.ReadLine()
	w := byteToInt(wBytes)

	for i := 0; i < w; i++ {
		word, _, _ := reader.ReadLine()
		wordTrie.insert(string(word))
	}

	_, _, _ = reader.ReadLine() // Remove empty line

	bBytes, _, _ := reader.ReadLine()
	b := byteToInt(bBytes)

	for i := 0; i < b; i++ {
		// Read boggle board
		for j := 0; j < 4; j++ {
			line, _, _ := reader.ReadLine()
			board[j] = []rune(string(line))
		}

		// If current line is not last line
		if i != b-1 {
			_, _, _ = reader.ReadLine() // Remove empty line
		}

		// Solve problem
		visited := make([][]bool, 4)
		for j := 0; j < 4; j++ {
			visited[j] = make([]bool, 4)
		}

		wordResult := make(map[string]struct{})
		for j := 0; j < 4; j++ {
			for k := 0; k < 4; k++ {
				dfs(location{j, k}, visited, wordTrie.root, make([]rune, 0), wordResult)
			}
		}

		// Print result
		score := 0
		longestWord := ""
		count := 0
		for word := range wordResult {
			wordLength := len(word)

			if wordLength > len(longestWord) {
				longestWord = word
			}

			if wordLength == len(longestWord) && strings.Compare(word, longestWord) < 0 {
				longestWord = word
			}

			switch wordLength {
			case 3, 4:
				score += 1
			case 5:
				score += 2
			case 6:
				score += 3
			case 7:
				score += 5
			case 8:
				score += 11
			}

			count++
		}

		writer.WriteString(strconv.Itoa(score) + " " + longestWord + " " + strconv.Itoa(count) + "\n")
	}
}
