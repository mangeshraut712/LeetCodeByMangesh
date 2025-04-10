from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort points by distance
        return sorted(points, key=lambda p: p[0]*p[0] + p[1]*p[1])[:k]