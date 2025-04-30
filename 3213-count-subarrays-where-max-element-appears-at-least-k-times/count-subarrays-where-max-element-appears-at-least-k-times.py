from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_elem = max(nums)
        count = 0
        left = 0
        freq = 0

        for right in range(len(nums)):
            if nums[right] == max_elem:
                freq += 1

            while freq >= k:
                # All subarrays starting at `left` and ending at `right`, `right+1`, ..., `n-1` are valid
                count += len(nums) - right
                if nums[left] == max_elem:
                    freq -= 1
                left += 1

        return count
