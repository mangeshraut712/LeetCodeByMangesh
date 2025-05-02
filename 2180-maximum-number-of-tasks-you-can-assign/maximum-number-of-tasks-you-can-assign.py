from collections import deque

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()                  # ascending
        workers.sort(reverse=True)    # descending
        n, m = len(tasks), len(workers)

        # bind to locals to avoid global lookups inside ok()
        ts, ws, p, s = tasks, workers, pills, strength
        deq = deque()

        def ok(k):
            """
            Can we assign the k easiest tasks (ts[0..k-1]) to
            the k strongest workers (ws[0..k-1]) using ≤ p pills?
            """
            deq.clear()
            rem, wi = p, 0
            # assign from hardest→easiest among those k tasks
            for ti in range(k - 1, -1, -1):
                req = ts[ti]
                # pull in every worker who, with a pill, could do this task
                while wi < m and ws[wi] + s >= req:
                    deq.append(ws[wi])
                    wi += 1

                if not deq:
                    return False

                # if the weakest candidate can do it unaided, use them
                if deq[0] >= req:
                    deq.popleft()
                # otherwise boost the strongest candidate
                elif rem:
                    deq.pop()
                    rem -= 1
                else:
                    return False

            return True

        # binary‐search on k = #tasks
        lo, hi, ans = 0, min(n, m), 0
        while lo <= hi:
            mid = (lo + hi) >> 1
            if ok(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
