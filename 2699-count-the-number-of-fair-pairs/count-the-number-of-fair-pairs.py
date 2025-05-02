from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n - 1):
            left_bound_j = bisect.bisect_left(nums, lower - nums[i], i + 1, n)
            right_bound_j = bisect.bisect_right(nums, upper - nums[i], i + 1, n)
            count += right_bound_j - left_bound_j

        return count
