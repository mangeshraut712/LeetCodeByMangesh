from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Or handle as per constraints/edge case definition
            
        current_max_sum = nums[0]
        global_max_sum = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            current_max_sum = max(num, current_max_sum + num)
            global_max_sum = max(global_max_sum, current_max_sum)
            
        return global_max_sum