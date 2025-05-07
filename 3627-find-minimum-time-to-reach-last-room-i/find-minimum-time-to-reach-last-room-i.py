import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        N = n * m
        mt = [t for row in moveTime for t in row]
        dist = [10**18] * N
        dist[0] = 0
        hq = [(0, 0)]
        heappush, heappop = heapq.heappush, heapq.heappop
        M = m

        while hq:
            t, u = heappop(hq)
            if t > dist[u]:
                continue
            if u == N - 1:
                return t
            # neighbors: up, down, left, right
            if u >= M:
                v = u - M
                nt = (t if t > mt[v] else mt[v]) + 1
                if nt < dist[v]:
                    dist[v] = nt
                    heappush(hq, (nt, v))
            if u + M < N:
                v = u + M
                nt = (t if t > mt[v] else mt[v]) + 1
                if nt < dist[v]:
                    dist[v] = nt
                    heappush(hq, (nt, v))
            if u % M:
                v = u - 1
                nt = (t if t > mt[v] else mt[v]) + 1
                if nt < dist[v]:
                    dist[v] = nt
                    heappush(hq, (nt, v))
            if u % M != M - 1:
                v = u + 1
                nt = (t if t > mt[v] else mt[v]) + 1
                if nt < dist[v]:
                    dist[v] = nt
                    heappush(hq, (nt, v))
        return -1
