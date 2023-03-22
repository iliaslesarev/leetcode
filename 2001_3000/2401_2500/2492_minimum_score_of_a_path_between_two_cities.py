import math
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        map = {}
        visited = [False] * (n + 1)
        for i in range(1, n + 1):
            map[i] = []

        for road in roads:
            map[road[0]].append((road[1], road[2]))
            map[road[1]].append((road[0], road[2]))

        min_cost = math.inf

        paths = [1]
        visited[1] = True
        while len(paths) != 0:
            node = paths.pop()
            for road in map[node]:
                if not visited[road[0]]:
                    paths.append(road[0])
                    visited[road[0]] = True
                min_cost = min(min_cost, road[1])
        return min_cost


print(Solution().minScore(n=4, roads=[[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))
print(Solution().minScore(n=4, roads=[[1, 2, 2], [1, 3, 4], [3, 4, 7]]))
print(Solution().minScore(n=2, roads=[[1, 2, 1]]))
print(Solution().minScore(n=9,
                          roads=[[1, 7, 1785], [7, 4, 1631], [3, 8, 5356], [4, 2, 9794], [5, 6, 7223], [8, 9, 1128],
                                 [2, 3, 8248]]))
