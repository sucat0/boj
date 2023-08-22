import sys

sys.setrecursionlimit(100000)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return

        cur_node = self.root

        while True:
            if cur_node == None:
                break

            if value < cur_node.value:
                if cur_node.left == None:
                    cur_node.left = Node(value)
                    break
                else:
                    cur_node = cur_node.left
            else:
                if cur_node.right == None:
                    cur_node.right = Node(value)
                    break
                else:
                    cur_node = cur_node.right
        
        cur_node = Node(value)

def postorder_print(bst: BST, cur_node = None):
    if cur_node == None:
        cur_node = bst.root
    
    if cur_node.left != None:
        postorder_print(bst, cur_node.left)
    if cur_node.right != None:
        postorder_print(bst, cur_node.right)
    print(cur_node.value)

inputs = sys.stdin.readlines()

bst = BST()
for i in inputs:
    j = int(i)
    bst.insert(j)

postorder_print(bst)