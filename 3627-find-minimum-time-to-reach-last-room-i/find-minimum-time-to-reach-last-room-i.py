import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        min_time = [[float('inf')] * m for _ in range(n)]
        min_time[0][0] = 0

        pq = [(0, 0, 0)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while pq:
            time_at_rc, r, c = heapq.heappop(pq)

            if time_at_rc > min_time[r][c]:
                continue

            if r == n - 1 and c == m - 1:
                return time_at_rc

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m:
                    # The earliest time you can be at the neighbor cell (nr, nc)
                    # is 1 second after the maximum of:
                    # 1. The time you are at the current cell (r, c).
                    # 2. The minimum time you can start moving TO cell (nr, nc).
                    time_to_be_at_neighbor = max(time_at_rc, moveTime[nr][nc]) + 1

                    if time_to_be_at_neighbor < min_time[nr][nc]:
                        min_time[nr][nc] = time_to_be_at_neighbor
                        heapq.heappush(pq, (time_to_be_at_neighbor, nr, nc))

        return -1
