import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        # Track visiting state: 0 = unvisited, 1 = being visited, 2 = visited
        visit = [0] * numCourses
        
        def dfs(course):
            if visit[course] == 1:  # Cycle detected
                return False
            if visit[course] == 2:  # Already processed
                return True
            
            visit[course] = 1  # Mark as being visited
            for next_course in adj[course]:
                if not dfs(next_course):
                    return False
            visit[course] = 2  # Mark as fully visited
            return True
        
        # Check for cycles starting from each unvisited course
        for course in range(numCourses):
            if visit[course] == 0 and not dfs(course):
                return False
        
        return True