from typing import List
from collections import deque

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort(reverse=True)

        n = len(tasks)
        m = len(workers)

        def can_assign(k: int) -> bool:
            if k == 0:
                return True

            task_idx = k - 1
            worker_idx = 0
            remaining_pills = pills
            pill_candidates = deque()

            while task_idx >= 0:
                current_task_req = tasks[task_idx]

                while worker_idx < m and workers[worker_idx] + strength >= current_task_req:
                    pill_candidates.append(workers[worker_idx])
                    worker_idx += 1

                if not pill_candidates:
                    return False

                if pill_candidates[0] >= current_task_req:
                    pill_candidates.popleft()
                elif remaining_pills > 0:
                    pill_candidates.pop()
                    remaining_pills -= 1
                else:
                    return False

                task_idx -= 1

            return True

        left, right = 0, min(n, m)
        best = 0

        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1

        return best
