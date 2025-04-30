from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        # Iterate through the array, considering subarrays of length 3
        # The loop goes up to len(nums) - 3 to ensure a valid subarray of length 3
        for i in range(len(nums) - 2):
            # Check if the middle element is even
            if nums[i+1] % 2 == 0:
                # Check the condition: sum of first and third equals half of the second
                if nums[i] + nums[i+2] == nums[i+1] // 2:
                    count += 1
        return count
