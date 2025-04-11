from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        operations = 0
        current_nums = list(nums)

        while not is_non_decreasing(current_nums) and len(current_nums) > 1:
            min_sum = float('inf')
            min_idx = 0

            for i in range(len(current_nums) - 1):
                current_sum = current_nums[i] + current_nums[i+1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    min_idx = i
            
            current_nums[min_idx] = current_nums[min_idx] + current_nums[min_idx+1]
            current_nums.pop(min_idx + 1)
            operations += 1

        return operations