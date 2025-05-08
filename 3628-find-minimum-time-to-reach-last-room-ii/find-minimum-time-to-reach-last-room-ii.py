import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        N = n * m
        # flatten the grid
        mt = [0] * N
        idx = 0
        for row in moveTime:
            for v in row:
                mt[idx] = v
                idx += 1

        INF = 10**18
        # dist[state], where state = (cell_index<<1) | parity
        dist = [INF] * (N * 2)
        # start at cell 0, parity=0 (next step cost = 1)
        dist[0] = 0
        hq = [(0, 0)]  # (time, state)
        pop, push = heapq.heappop, heapq.heappush

        while hq:
            t, s = pop(hq)
            if t != dist[s]:
                continue
            u = s >> 1
            if u == N - 1:
                return t
            # current parity and step cost
            parity = s & 1
            c = 1 if parity == 0 else 2
            new_parity = parity ^ 1

            row_mod = u % m

            # up
            v = u - m
            if v >= 0:
                nt = t if t >= mt[v] else mt[v]
                nt += c
                ns = (v << 1) | new_parity
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

            # down
            v = u + m
            if v < N:
                nt = t if t >= mt[v] else mt[v]
                nt += c
                ns = (v << 1) | new_parity
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

            # left
            if row_mod != 0:
                v = u - 1
                nt = t if t >= mt[v] else mt[v]
                nt += c
                ns = (v << 1) | new_parity
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

            # right
            if row_mod != m - 1:
                v = u + 1
                nt = t if t >= mt[v] else mt[v]
                nt += c
                ns = (v << 1) | new_parity
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

        return -1
