import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        N = n * m
        mt = [0] * N
        idx = 0
        for row in moveTime:
            for v in row:
                mt[idx] = v
                idx += 1

        INF = 10**18
        dist = [INF] * (N * 2)
        dist[0] = 0
        hq = [(0, 0)]
        pop, push = heapq.heappop, heapq.heappush

        while hq:
            t, s = pop(hq)
            if t != dist[s]:
                continue
            u = s >> 1
            if u == N - 1:
                return t
            parity = s & 1
            c = 1 if parity == 0 else 2
            new_parity = parity ^ 1

            row_mod = u % m

            v = u - m
            if v >= 0:
                nt = t if t >= mt[v] else mt[v]
                nt += c
                ns = (v << 1) | new_parity
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

            v = u + m
            if v < N:
                nt = t if t >= mt[v] else mt[v]
                nt += c
                ns = (v << 1) | new_parity
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

            if row_mod != 0:
                v = u - 1
                nt = t if t >= mt[v] else mt[v]
                nt += c
                ns = (v << 1) | new_parity
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

            if row_mod != m - 1:
                v = u + 1
                nt = t if t >= mt[v] else mt[v]
                nt += c
                ns = (v << 1) | new_parity
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

        return -1
