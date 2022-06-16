from sys import stdin
from collections import deque
import pprint


class Infection:
    @staticmethod
    def find_near_node(node: tuple[int, int], x_max, y_max):
        node_x = node[0]
        node_y = node[1]

        is_at_left = node_x <= 0
        is_at_right = node_x >= x_max
        is_at_up = node_y <= 0
        is_at_down = node_y >= y_max

        if not is_at_left:
            yield node_x - 1, node_y

        if not is_at_right:
            yield node_x + 1, node_y

        if not is_at_up:
            yield node_x, node_y - 1

        if not is_at_down:
            yield node_x, node_y + 1

    @staticmethod
    def bfs(lab_map: list[list[int]], virus: list[tuple[int, int]], lab_x: int, lab_y: int):
        queue = deque(virus)
        infection_count = 0

        while queue:
            node = queue.popleft()
            for near_node_x, near_node_y in Infection.find_near_node(node, lab_x, lab_y):
                near_node = lab_map[near_node_y][near_node_x]
                if near_node != 2 and near_node != 1:
                    pprint.pprint(lab_map)
                    queue.append((near_node_x, near_node_y))
                    lab_map[near_node_y][near_node_x] = 2

                    infection_count += 1

        return infection_count


def main():
    lab_y, lab_x = map(int, stdin.readline().split())

    virus = []
    lab_map = []
    for node_y in range(lab_y):
        str_node_list = stdin.readline().split()
        node_list = []
        for node_x, node in enumerate(str_node_list):
            if node == '2':
                virus.append((node_x, node_y))

            node_list.append(int(node))
        lab_map.append(node_list)

    print(Infection.bfs(lab_map, virus, lab_x-1, lab_y-1))


if __name__ == '__main__':
    main()
