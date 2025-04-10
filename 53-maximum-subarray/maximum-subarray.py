from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxCrossingSum(nums, left, mid, right):
            # Maximum sum crossing to the left, including elements up to mid
            left_sum = float('-inf')
            current_sum = 0
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)
            
            # Maximum sum crossing to the right, starting from mid + 1
            right_sum = float('-inf')
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)
            
            return left_sum + right_sum
        
        def maxSubArrayHelper(nums, left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            left_max = maxSubArrayHelper(nums, left, mid)
            right_max = maxSubArrayHelper(nums, mid + 1, right)
            cross_max = maxCrossingSum(nums, left, mid, right)
            
            return max(left_max, right_max, cross_max)
        
        return maxSubArrayHelper(nums, 0, len(nums) - 1)