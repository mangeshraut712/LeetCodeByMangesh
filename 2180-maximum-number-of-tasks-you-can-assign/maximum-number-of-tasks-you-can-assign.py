from collections import deque

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()  # Sort tasks in ascending order (easiest to hardest)
        workers.sort(reverse=True)  # Sort workers in descending order (strongest to weakest)

        n = len(tasks)
        m = len(workers)

        # Helper function to check if it's possible to assign k tasks
        def can_assign(k):
            if k == 0:
                return True

            # We consider the k easiest tasks and try to assign them to k of the m strongest workers.
            # We will iterate through the k easiest tasks from hardest to easiest.
            task_idx = k - 1  # Start with the hardest of the k tasks
            worker_idx = 0    # Pointer for the strongest available workers
            remaining_pills = pills
            # Deque to store workers who are strong enough to complete the current task
            # (possibly with a pill). Workers are added in order of strength (descending).
            pill_candidates = deque()

            # Iterate through the k easiest tasks from hardest to easiest
            while task_idx >= 0:
                current_task_req = tasks[task_idx]

                # Add strongest available workers who can potentially do the current task
                # (with or without a pill) to the pill_candidates deque.
                # Since workers are sorted descending, appending from worker_idx maintains
                # stronger workers at the back of the deque.
                while worker_idx < m and workers[worker_idx] + strength >= current_task_req:
                    pill_candidates.append(workers[worker_idx])
                    worker_idx += 1

                # If there are no workers who can do this task (even with a pill), we fail
                if not pill_candidates:
                    return False

                # Now, from the available workers in pill_candidates, try to assign the task.
                # Greedy strategy:
                # 1. Check if the weakest worker in pill_candidates (front of deque) can do the task without a pill.
                #    If yes, use that worker. This is the most efficient use of a worker.
                if pill_candidates[0] >= current_task_req:
                    pill_candidates.popleft()
                # 2. If the weakest cannot, but we have pills left, use a pill on the strongest
                #    worker in pill_candidates (back of deque). This uses a pill efficiently
                #    on a worker who needs it for this task, reserving weaker pill-candidates
                #    for potentially easier tasks later.
                elif remaining_pills > 0:
                    pill_candidates.pop()
                    remaining_pills -= 1
                # 3. If neither of the above is possible, we cannot assign the current task.
                else:
                    return False

                # Move to the next easiest task
                task_idx -= 1

            # If we successfully assigned all k tasks, return True
            return True

        # Binary search for the maximum number of tasks (k) that can be assigned
        # The possible number of tasks ranges from 0 to min(n, m).
        left, right = 0, min(n, m)
        best = 0

        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                # If mid tasks can be assigned, it's possible to do at least mid tasks.
                # Store mid as a potential best answer and try for more tasks.
                best = mid
                left = mid + 1
            else:
                # If mid tasks cannot be assigned, then we need to try fewer tasks.
                right = mid - 1

        return best
