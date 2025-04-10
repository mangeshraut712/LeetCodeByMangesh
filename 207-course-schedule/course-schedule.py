import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        queue = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])
        courses_taken = 0

        while queue:
            prereq = queue.popleft()
            courses_taken += 1
            for course in adj[prereq]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        return courses_taken == numCourses
