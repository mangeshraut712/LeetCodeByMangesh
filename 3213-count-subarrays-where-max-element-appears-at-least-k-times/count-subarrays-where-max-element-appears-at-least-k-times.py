from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        top = max(nums)
        left = 0
        window = 0

        for right in range(len(nums)):
            if nums[right] == top:
                window += 1

            while window >= k:
                if nums[left] == top:
                    window -= 1
                left += 1

            # When the window [left, right] contains at least k occurrences of 'top',
            # any subarray ending at 'right' and starting from index 0 up to 'left - 1'
            # is a valid subarray. The number of such starting positions is 'left'.
            # If the `while` loop condition was `window >= k` and we exit it, it means
            # the current window `[left, right]` has `window < k`.
            # The valid subarrays ending at `right` are those starting from index 0 up to `left - 1`.
            # The number of such subarrays is `left`.
            count += left

        return count
