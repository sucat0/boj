from sys import stdin


class Graph:
    def __init__(self, connections, node_num):
        self.graph: list[list[int]] = [[] for _ in range(node_num+1)]
        self.parents = [0] * (node_num+1)

        for node_one, node_two in connections:
            self.graph[node_one].append(node_two)
            self.graph[node_two].append(node_one)

    def find_parents(self, start_node):
        visited = []
        queue = [start_node]

        while queue:
            node = queue.pop()

            if node not in visited:
                visited.append(node)

                connected_nodes = self.graph[node]
                for connected_node in connected_nodes:
                    if self.parents[connected_node] == 0:
                        self.parents[connected_node] = node
                queue.extend(connected_nodes)

        return self.parents


def main():
    n = int(stdin.readline().rstrip())
    connections = [map(int, stdin.readline().split()) for _ in range(n-1)]

    graph = Graph(connections, n)
    parents = graph.find_parents(1)

    for node_num in range(2, n+1):
        print(parents[node_num])


if __name__ == '__main__':
    main()
