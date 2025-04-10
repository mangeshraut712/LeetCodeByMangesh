import collections
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)
            
        result = []
        for i in range(n, 0, -1):
            if buckets[i]:
                result.extend(buckets[i])
            if len(result) >= k:
                break
                
        return result[:k]