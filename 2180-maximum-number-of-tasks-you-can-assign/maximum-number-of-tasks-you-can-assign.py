from collections import deque
from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()  # Sort tasks in ascending order
        workers.sort()  # Sort workers in ascending order

        n = len(tasks)
        m = len(workers)

        # Helper function to check if it's possible to assign k tasks
        def can_assign(k):
            if k == 0:
                return True

            # We consider the k easiest tasks and the k strongest workers from the available m workers
            # We will try to assign the k easiest tasks to k of the m strongest workers
            current_tasks = tasks[:k]
            # Use a SortedList for the k strongest workers for efficient searching and removal
            current_workers = SortedList(workers[m - k:])

            remaining_pills = pills

            # Iterate through the k easiest tasks from hardest to easiest
            for task_idx in range(k - 1, -1, -1):
                current_task_req = current_tasks[task_idx]

                # Greedy strategy:
                # 1. Try to find the weakest worker in current_workers who can do the task WITHOUT a pill
                #    bisect_left finds the index where current_task_req would be inserted to maintain order.
                #    If the element at that index exists and is >= current_task_req, that's the weakest worker.
                worker_idx = current_workers.bisect_left(current_task_req)

                if worker_idx < len(current_workers):
                    # Found a worker who can do it without a pill, use them.
                    current_workers.pop(worker_idx)
                else:
                    # No worker can do it without a pill. Check if we can use a pill.
                    if remaining_pills > 0:
                        # Find the weakest worker who can do the task WITH a pill.
                        # This worker needs strength >= current_task_req - strength.
                        pill_worker_idx = current_workers.bisect_left(current_task_req - strength)

                        if pill_worker_idx < len(current_workers):
                            # Found a worker who can do it with a pill, use them and a pill.
                            current_workers.pop(pill_worker_idx)
                            remaining_pills -= 1
                        else:
                            # No worker can do this task even with a pill. Cannot assign k tasks.
                            return False
                    else:
                        # No pills left and no worker can do it without a pill. Cannot assign k tasks.
                        return False

            # If we successfully assigned all k tasks, return True
            return True

        # Binary search for the maximum number of tasks (k) that can be assigned
        left, right = 0, min(n, m)
        best = 0

        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                # If mid tasks can be assigned, try for more
                best = mid
                left = mid + 1
            else:
                # If mid tasks cannot be assigned, try fewer
                right = mid - 1

        return best
