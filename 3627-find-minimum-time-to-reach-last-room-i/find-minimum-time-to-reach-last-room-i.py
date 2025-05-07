import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        INF = 10**18
        dist = [[INF]*m for _ in range(n)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        push, pop = heapq.heappush, heapq.heappop

        while heap:
            t, i, j = pop(heap)
            if t > dist[i][j]:
                continue
            if i == n-1 and j == m-1:
                return t
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m:
                    # can start moving into (ni,nj) no earlier than moveTime[ni][nj],
                    # then moving takes 1 second
                    nt = max(t, moveTime[ni][nj]) + 1
                    if nt < dist[ni][nj]:
                        dist[ni][nj] = nt
                        push(heap, (nt, ni, nj))

        return dist[n-1][m-1]
