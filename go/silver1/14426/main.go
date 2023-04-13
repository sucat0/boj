package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

type trieNode struct {
	child map[rune]*trieNode
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
}

func (t *trie) checkInSet(word string) bool {
	node := t.root

	for _, d := range word {
		if node.child == nil {
			return false
		}

		if node.child[d] == nil {
			return false
		}

		node = node.child[d]
	}

	return true
}

func bytesToInt(b []byte) (int, int) {
	var n, m int
	var split int
	for i, c := range b {
		if c == ' ' {
			split = i
			break
		}
		n = n*10 + int(c-'0')
	}

	for _, c := range b[split+1:] {
		m = m*10 + int(c-'0')
	}

	return n, m
}

func main() {
	defer writer.Flush()

	lineBytes, _, _ := reader.ReadLine()
	n, m := bytesToInt(lineBytes)

	trie := newTrie()
	for i := 0; i < n; i++ {
		lineBytes, _, _ := reader.ReadLine()
		trie.insert(string(lineBytes))
	}

	var count int
	for i := 0; i < m; i++ {
		lineBytes, _, _ := reader.ReadLine()
		if trie.checkInSet(string(lineBytes)) {
			count++
		}
	}

	writer.WriteString(strconv.Itoa(count))
}
