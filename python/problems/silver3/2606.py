from collections import deque
from sys import stdin


class SearchVirus:
    @staticmethod
    def connection_graph_conv(pc_num: int, connections: list[list]) -> list[set]:
        graph = [None] + [set() for _ in range(pc_num)]  # index starts with 1

        for pc1, pc2 in connections:
            graph[pc1].add(pc2)
            graph[pc2].add(pc1)

        
        return graph

    @staticmethod
    def bfs(pc_num: int, graph: list[set], epicenter: int):
        queue = deque([epicenter])
        visited = [None] + [False]*pc_num  # index starts with 1
        visited[epicenter] = True
        infected = 0

        while queue:
            search_pc = queue.popleft()

            for connected_pc in graph[search_pc]:
                if not visited[connected_pc]:
                    queue.append(connected_pc)
                    visited[connected_pc] = True
                    infected += 1

        return infected


pc_num = int(stdin.readline().rstrip())
connection_num = int(stdin.readline().rstrip())
connections = [map(int, stdin.readline().split()) for _ in range(connection_num)]

graph = SearchVirus.connection_graph_conv(pc_num, connections)
infected = SearchVirus.bfs(pc_num, graph, 1)

print(infected)
