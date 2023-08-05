import sys

input = sys.stdin.readline 

tree = [[] for _ in range(100001)]

v = int(input())
for _ in range(v):
    data = list(map(int, input().split()))

    cur_node_num = data[0]

    node_num = 0
    for i in data[1:-1]:
        if node_num == 0: 
            node_num = i
            continue

        tree[cur_node_num].append((node_num, i))
        node_num = 0

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
