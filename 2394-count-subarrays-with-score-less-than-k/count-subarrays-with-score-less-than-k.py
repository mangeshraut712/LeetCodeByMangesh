from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        Counts the number of non-empty subarrays whose score (sum * length) is strictly less than k.

        Uses a sliding window approach to efficiently count valid subarrays.

        Args:
            nums: A list of positive integers.
            k: An integer representing the maximum allowed score + 1.

        Returns:
            The number of subarrays with a score strictly less than k.
        """
        count = 0
        left = 0
        current_sum = 0
        n = len(nums)

        # Iterate through the array with the right pointer
        for right in range(n):
            # Expand the window by adding the current element
            current_sum += nums[right]

            # While the score of the current window is not less than k, shrink the window from the left
            # The score is current_sum * (length of the window)
            while current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1

            # At this point, the score of the window [left, right] is less than k.
            # Any subarray ending at 'right' and starting from 'left' up to 'right' is valid.
            # The number of such subarrays is (right - left + 1).
            count += (right - left + 1)

        return count
