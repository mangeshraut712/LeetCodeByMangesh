from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max_sum = nums[0]
        global_max_sum = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            current_max_sum = max(num, current_max_sum + num)
            global_max_sum = max(global_max_sum, current_max_sum)
            
        return global_max_sum