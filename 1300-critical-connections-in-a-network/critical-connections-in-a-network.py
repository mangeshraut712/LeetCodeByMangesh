import sys
from typing import List
from collections import defaultdict

sys.setrecursionlimit(10**7)

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n
        low = [-1] * n
        timer = 0
        critical_bridges = []

        def dfs(node, parent):
            nonlocal timer
            disc[node] = timer
            low[node] = timer
            timer += 1

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if disc[neighbor] == -1:
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > disc[node]:
                        critical_bridges.append([node, neighbor])
                else:
                    low[node] = min(low[node], disc[neighbor])

        # The problem constraints guarantee a connected graph (n-1 <= connections.length),
        # so starting DFS from node 0 is sufficient.
        dfs(0, -1)

        return critical_bridges
