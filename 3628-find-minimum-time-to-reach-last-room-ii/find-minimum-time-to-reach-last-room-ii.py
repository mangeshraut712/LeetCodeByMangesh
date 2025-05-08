import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        N = n * m
        # flatten grid
        mt = [t for row in moveTime for t in row]
        # visited flags
        vis = [False] * N
        # min-heap of (time, idx, next_step_cost)
        hq = [(0, 0, 1)]
        pop, push = heapq.heappop, heapq.heappush
        M = m

        while hq:
            t, u, c = pop(hq)
            if vis[u]:
                continue
            vis[u] = True
            if u == N - 1:
                return t
            # base time after waiting for unlock
            for v in (u - M, u + M, u - 1, u + 1):
                # bounds check
                if not (0 <= v < N):
                    continue
                # prevent row wrap
                if (v == u - 1 and u % M == 0) or (v == u + 1 and u % M == M - 1):
                    continue
                # earliest we can enter v
                nt = t if t >= mt[v] else mt[v]
                nt += c
                push(hq, (nt, v, 3 - c))
        return -1
