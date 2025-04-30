from typing import List
from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)

        count = 0
        last_max_indices = deque()

        for right in range(len(nums)):
            if nums[right] == max_val:
                last_max_indices.append(right)

            if len(last_max_indices) >= k:
                count += last_max_indices[len(last_max_indices) - k] + 1

        return count
