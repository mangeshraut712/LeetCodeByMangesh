import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        N = n * m

        # Flatten grid into a single list for O(1) indexing
        mt = [0] * N
        idx = 0
        for row in moveTime:
            for v in row:
                mt[idx] = v
                idx += 1

        INF = 10**18
        # dist[state] where state = (cell_index << 1) | parity_bit
        # parity_bit = 0 → next move costs 1s; parity_bit = 1 → next move costs 2s
        dist = [INF] * (N * 2)
        dist[0] = 0    # start at cell 0 with parity_bit=0

        hq = [(0, 0)]  # (time, state)
        pop, push = heapq.heappop, heapq.heappush
        M = m

        while hq:
            t, s = pop(hq)
            if t != dist[s]:
                continue

            u = s >> 1
            if u == N - 1:
                return t

            # decode parity → step cost → next parity
            if (s & 1) == 0:
                c = 1; np = 1
            else:
                c = 2; np = 0

            row_mod = u % M
            base = t

            # Up
            v = u - M
            if v >= 0:
                nt = base if base >= mt[v] else mt[v]
                nt += c
                ns = (v << 1) | np
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

            # Down
            v = u + M
            if v < N:
                nt = base if base >= mt[v] else mt[v]
                nt += c
                ns = (v << 1) | np
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

            # Left
            if row_mod:
                v = u - 1
                nt = base if base >= mt[v] else mt[v]
                nt += c
                ns = (v << 1) | np
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

            # Right
            if row_mod != M - 1:
                v = u + 1
                nt = base if base >= mt[v] else mt[v]
                nt += c
                ns = (v << 1) | np
                if nt < dist[ns]:
                    dist[ns] = nt
                    push(hq, (nt, ns))

        # should never get here per problem constraints
        return -1
