from bisect import bisect_left
from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def can_assign(k: int) -> bool:
            # Try to assign the k smallest tasks to the k strongest workers.
            if k == 0:
                return True
            
            T = tasks[:k]               # smallest k tasks, sorted
            W = workers[-k:]            # strongest k workers, sorted
            rem_pills = pills
            
            # Process tasks from largest to smallest
            for t in reversed(T):
                # 1) If our strongest worker can do it unaided, use them.
                if W and W[-1] >= t:
                    W.pop()
                else:
                    # 2) Otherwise we must use a pill.  Find the smallest w s.t. w+strength >= t
                    if rem_pills == 0:
                        return False
                    need = t - strength
                    # lower_bound on W
                    i = bisect_left(W, need)
                    if i == len(W):
                        return False
                    # give the pill to W[i]
                    W.pop(i)
                    rem_pills -= 1
            
            return True
        
        # Binary‑search the maximum k we can feasibly assign
        lo, hi = 0, min(len(tasks), len(workers))
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_assign(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
