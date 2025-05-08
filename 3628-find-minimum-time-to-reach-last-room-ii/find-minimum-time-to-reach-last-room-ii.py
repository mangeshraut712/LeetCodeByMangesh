import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n = len(moveTime); m = len(moveTime[0])
        N = n * m
        mt = [0] * N
        idx = 0
        for row in moveTime:
            for v in row:
                mt[idx] = v
                idx += 1

        INF = 10**30
        dist = [INF] * (N * 2)
        dist[0] = 0
        hq = [(0, 0)]
        push, pop = heapq.heappush, heapq.heappop
        target = N - 1

        while hq:
            t, s = pop(hq)
            if t != dist[s]:
                continue
            i, par = s >> 1, s & 1
            if i == target:
                return t
            c = 1 if par == 0 else 2

            # up
            if i >= m:
                v = i - m
                nt = t if t > mt[v] else mt[v]
                nt += c
                ns = (v << 1) | (par ^ 1)
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

            # down
            v = i + m
            if v < N:
                nt = t if t > mt[v] else mt[v]
                nt += c
                ns = (v << 1) | (par ^ 1)
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

            # left/right
            j = i % m
            if j:
                v = i - 1
                nt = t if t > mt[v] else mt[v]
                nt += c
                ns = (v << 1) | (par ^ 1)
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))
            if j < m - 1:
                v = i + 1
                nt = t if t > mt[v] else mt[v]
                nt += c
                ns = (v << 1) | (par ^ 1)
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

        return -1
