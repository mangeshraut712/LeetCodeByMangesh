import collections
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        count = collections.Counter(nums)
        
        # Step 2: Use a min-heap to keep the top k elements
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Step 3: Extract the numbers from the heap
        return [num for _, num in heap]