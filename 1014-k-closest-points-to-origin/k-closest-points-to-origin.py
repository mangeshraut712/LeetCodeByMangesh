import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points:
            dist_sq = -(x*x + y*y)  # Negate for max-heap simulation
            
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist_sq, x, y))
            elif dist_sq > max_heap[0][0]:  # Current point is closer
                heapq.heapreplace(max_heap, (dist_sq, x, y))
        
        return [[x, y] for _, x, y in max_heap]