package main

import (
	"bufio"
	"os"
	"sort"
	"strings"
)

var (
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

type trieNode struct {
	child map[string]*trieNode
}

type trie struct {
	root *trieNode
}

func newTrie() *trie {
	return &trie{root: &trieNode{}}
}

func (t *trie) insert(foods []string) {
	node := t.root

	for _, food := range foods {
		if node.child == nil {
			node.child = make(map[string]*trieNode)
		}

		if node.child[food] == nil {
			node.child[food] = &trieNode{}
		}

		node = node.child[food]
	}
}

func (t *trie) print(node *trieNode, depth int) {
	k := make([]string, 0, len(node.child))
	for key := range node.child {
		k = append(k, key)
	}

	sort.Strings(k)

	for _, key := range k {
		for i := 0; i < depth; i++ {
			writer.WriteString("--")
		}
		writer.WriteString(key)
		writer.WriteByte('\n')

		t.print(node.child[key], depth+1)
	}
}

func byteToInt(b []byte) int {
	var i int
	for _, c := range b {
		i *= 10
		i += int(c - '0')
	}

	return i
}

func main() {
	defer writer.Flush()

	trie := newTrie()
	nByte, _, _ := reader.ReadLine()
	n := byteToInt(nByte)
	for i := 0; i < n; i++ {
		line, _, _ := reader.ReadLine()
		lines := strings.Split(string(line), " ")[1:]
		trie.insert(lines)
	}

	trie.print(trie.root, 0)
}
