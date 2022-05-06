from sys import stdin

class Hashtable:
    def __init__(self, min_index:int, max_index:int) -> None:
        self.hash_table = [0 for _ in range(min_index-max_index)]

    def add_data(self, value:str) -> None:
        


n, m = stdin.readline()

for 