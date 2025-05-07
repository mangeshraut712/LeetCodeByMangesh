import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime); m = len(moveTime[0])
        N = n * m
        # flatten moveTime into a 1D list
        mt = [0] * N
        for i in range(n):
            base = i * m
            row = moveTime[i]
            for j in range(m):
                mt[base + j] = row[j]

        INF = 10**18
        dist = [INF] * N
        dist[0] = 0
        heap = [(0, 0)]
        push, pop = heapq.heappush, heapq.heappop
        end = N - 1

        while heap:
            t, u = pop(heap)
            if u == end:
                return t
            if t > dist[u]:
                continue

            # try each of the 4 neighbors
            # up
            v = u - m
            if v >= 0:
                mv = mt[v]
                nt = t + 1 if t >= mv else mv + 1
                if nt < dist[v]:
                    dist[v] = nt
                    push(heap, (nt, v))
            # down
            v = u + m
            if v < N:
                mv = mt[v]
                nt = t + 1 if t >= mv else mv + 1
                if nt < dist[v]:
                    dist[v] = nt
                    push(heap, (nt, v))
            # left
            if u % m:
                v = u - 1
                mv = mt[v]
                nt = t + 1 if t >= mv else mv + 1
                if nt < dist[v]:
                    dist[v] = nt
                    push(heap, (nt, v))
            # right
            if u % m < m - 1:
                v = u + 1
                mv = mt[v]
                nt = t + 1 if t >= mv else mv + 1
                if nt < dist[v]:
                    dist[v] = nt
                    push(heap, (nt, v))

        return dist[end]
