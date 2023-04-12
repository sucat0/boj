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

func (t *trie) insert(dir []string) {
	node := t.root

	for _, d := range dir {
		if node.child == nil {
			node.child = make(map[string]*trieNode)
		}

		if node.child[d] == nil {
			node.child[d] = &trieNode{}
		}

		node = node.child[d]
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
			writer.WriteString(" ")
		}
		writer.WriteString(key)
		writer.WriteByte('\n')

		t.print(node.child[key], depth+1)
	}
}

func main() {
	defer writer.Flush()

	trie := newTrie()
	nByte, _, _ := reader.ReadLine()
	n, _ := strconv.Atoi(string(nByte))

	for i := 0; i < n; i++ {
		line, _, _ := reader.ReadLine()
		trie.insert(strings.Split(string(line), "\\"))
	}

	trie.print(trie.root, 0)
}
