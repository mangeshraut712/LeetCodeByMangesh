from bisect import bisect_left
from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)

        def can_assign(k: int) -> bool:
            """
            Return True if we can assign the k easiest tasks (tasks[0..k-1])
            to the k strongest workers (workers[m-k..m-1]) using ≤ pills boosts.
            """
            if k == 0:
                return True

            # Take the k smallest tasks, and the k largest workers
            T = tasks[:k]            # sorted ascending
            W = workers[m-k:]        # sorted ascending
            rem = pills

            # Try to assign from hardest→easiest
            for req in reversed(T):
                # 1) If our strongest remaining worker can do it unaided, use them.
                if W and W[-1] >= req:
                    W.pop()
                else:
                    # 2) Otherwise we must use a pill.
                    if rem == 0:
                        return False
                    # Find the *smallest* w in W s.t. w + strength >= req
                    need = req - strength
                    i = bisect_left(W, need)
                    if i == len(W):
                        return False
                    # Use that worker with a pill
                    W.pop(i)
                    rem -= 1

            return True

        # Binary‑search the max k ∈ [0, min(n,m)] we can assign
        lo, hi, ans = 0, min(n, m), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_assign(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
