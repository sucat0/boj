package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

var (
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

type trieNode struct {
	child      map[rune]*trieNode
	childCount int // For faster checking?
	isEnd      bool
}

type trie struct {
	root *trieNode
}

func newTrie() *trie {
	return &trie{root: &trieNode{child: make(map[rune]*trieNode)}}
}

func (t *trie) insert(word string) {
	node := t.root

	for _, c := range word {
		if node.child[c] == nil {
			node.child[c] = &trieNode{child: make(map[rune]*trieNode)}
			node.childCount++
		}

		node = node.child[c]
	}

	node.isEnd = true
}

func (t *trie) autocomplete(word string) (pressCount int) {
	node := t.root.child[rune(word[0])]

	count := 1
	for _, c := range word[1:] {
		if node.childCount == 1 && !node.isEnd {
			node = node.child[c]
			continue
		}

		node = node.child[c]
		count++
	}

	return count
}

func main() {
	defer writer.Flush()

	// Read until EOF
	for {
		var n int
		if nBytes, _, err := reader.ReadLine(); err != nil {
			break
		} else {
			n, _ = strconv.Atoi(string(nBytes))
		}

		// Insert words to trie
		words := make([]string, n)
		t := newTrie()
		for i := 0; i < n; i++ {
			wordBytes, _, _ := reader.ReadLine()
			word := string(wordBytes)

			t.insert(word)
			words[i] = word
		}

		// Find button press count
		var sum int
		for _, word := range words {
			sum += t.autocomplete(word)
		}

		// Print average
		avg := math.Round(float64(sum)/float64(n)*100) / 100

		writer.WriteString(strconv.FormatFloat(avg, 'f', 2, 64))
		writer.WriteByte('\n')
	}
}
