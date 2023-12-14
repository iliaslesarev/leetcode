from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def helper(city, visited):
            visited[city] = True
            for neighbor in adj[city]:
                if not visited[neighbor]:
                    outward_connections.add((city, neighbor))
                    helper(neighbor, visited)

        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        outward_connections = set()

        helper(0, [False] * n)
        needs_change = 0
        for a, b in connections:
            if (a, b) in outward_connections:
                needs_change += 1
        return needs_change
