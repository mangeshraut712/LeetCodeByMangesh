from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for num in nums:
            if num < k:
                return -1

        distinct_greater_than_k = set()
        for num in nums:
            if num > k:
                distinct_greater_than_k.add(num)

        return len(distinct_greater_than_k)
