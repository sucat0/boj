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

type treeNode struct {
	left  *treeNode
	right *treeNode

	value rune
}

type tree struct {
	root *treeNode
}

func newTree() *tree {
	return &tree{}
}

func insert(node *treeNode, value, left, right rune) {
	if node == nil {
		return
	}

	if node.value == value {
		if left != '.' {
			node.left = &treeNode{value: left}
		}

		if right != '.' {
			node.right = &treeNode{value: right}
		}
	} else {
		// Search
		insert(node.left, value, left, right)
		insert(node.right, value, left, right)
	}
}

func (t *tree) preorder(node *treeNode) {
	writer.WriteRune(node.value)

	if node.left != nil {
		t.preorder(node.left)
	}

	if node.right != nil {
		t.preorder(node.right)
	}
}

func (t *tree) inorder(node *treeNode) {
	if node.left != nil {
		t.inorder(node.left)
	}

	writer.WriteRune(node.value)

	if node.right != nil {
		t.inorder(node.right)
	}
}

func (t *tree) postorder(node *treeNode) {
	if node.left != nil {
		t.postorder(node.left)
	}

	if node.right != nil {
		t.postorder(node.right)
	}

	writer.WriteRune(node.value)
}

func main() {
	defer writer.Flush()

	nByte, _, _ := reader.ReadLine()
	n, _ := strconv.Atoi(string(nByte))

	t := newTree()
	t.root = &treeNode{value: 'A'}

	for i := 0; i < n; i++ {
		nodeByte, _, _ := reader.ReadLine()
		nodeStr := strings.Split(string(nodeByte), " ")

		insert(t.root, rune(nodeStr[0][0]), rune(nodeStr[1][0]), rune(nodeStr[2][0]))
	}

	t.preorder(t.root)
	writer.WriteString("\n")
	t.inorder(t.root)
	writer.WriteString("\n")
	t.postorder(t.root)
}
