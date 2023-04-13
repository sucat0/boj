package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

type trieNode struct {
	children [10]*trieNode
	isEnd    bool
}

type trie struct {
	root *trieNode
}

func newTrie() *trie {
	return &trie{root: &trieNode{}}
}

func (t *trie) insert(phoneNum string) bool {
	if t.root == nil {
		t.root = &trieNode{}
	}

	node := t.root

	for i := range phoneNum {
		d := phoneNum[i] - '0'

		if node.children[d] == nil {
			node.children[d] = &trieNode{}
		}

		if node.children[d].isEnd {
			return false
		}

		node = node.children[d]
	}

	node.isEnd = true
	return true
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	tbyte, _, _ := reader.ReadLine()
	t, _ := strconv.Atoi(string(tbyte))
	for i := 0; i < t; i++ {
		var notConsistent bool
		nbyte, _, _ := reader.ReadLine()
		n, _ := strconv.Atoi(string(nbyte))

		trie := newTrie()
		var buf []string
		for j := 0; j < n; j++ {
			pbyte, _, _ := reader.ReadLine()
			buf = append(buf, string(pbyte))
		}

		sort.Strings(buf)

		for j := 0; j < n; j++ {
			n := buf[j]
			if !trie.insert(n) {
				notConsistent = true
				break
			}
		}

		if notConsistent {
			writer.WriteString("NO\n")
		} else {
			writer.WriteString("YES\n")
		}
	}
}
