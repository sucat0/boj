import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
tree = [[] for _ in range(10001)]

for _ in range(n-1):
    parent, child, w = map(int, input().split())

    tree[parent].append((child, w))
    tree[child].append((parent, w))

def find_longest(cur_node, sum_dist = 0, last_node = 0):
    if len(tree[cur_node]) == 1 and last_node == tree[cur_node][0][0]:
        return cur_node, sum_dist

    res_node, res_dist = 0, 0
    for next_node, dist in tree[cur_node]:
        if next_node == last_node: continue

        end_node, end_dist = find_longest(next_node, sum_dist+dist, cur_node)

        if res_dist < end_dist:
            res_node, res_dist = end_node, end_dist

    return res_node, res_dist

res_node, _ = find_longest(1)
_, res_dist = find_longest(res_node)
print(res_dist)
