import collections
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        count = collections.Counter(nums)
        n = len(nums)
        
        # Step 2: Bucket sort by frequency
        buckets = [[] for _ in range(n + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # Step 3: Collect top k elements
        result = []
        for freq in range(n, 0, -1):
            if len(result) >= k:
                break
            if buckets[freq]:
                result.extend(buckets[freq])
        
        return result[:k]