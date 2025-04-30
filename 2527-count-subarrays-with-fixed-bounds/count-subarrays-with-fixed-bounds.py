from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        Counts the number of subarrays that have both minK and maxK as their minimum and maximum elements.

        Args:
            nums: The input integer array.
            minK: The required minimum value in a fixed-bound subarray.
            maxK: The required maximum value in a fixed-bound subarray.

        Returns:
            The total count of fixed-bound subarrays.
        """
        count = 0
        # left_bound marks the start of the current valid window (elements are within [minK, maxK])
        left_bound = -1
        # last_minK stores the index of the most recent occurrence of minK
        last_minK = -1
        # last_maxK stores the index of the most recent occurrence of maxK
        last_maxK = -1

        for right in range(len(nums)):
            # If the current element is outside the [minK, maxK] range,
            # it breaks any potential fixed-bound subarray ending at or before 'right'.
            # We update the left_bound to the next position.
            if nums[right] < minK or nums[right] > maxK:
                left_bound = right
            # Update the last seen index for minK
            if nums[right] == minK:
                last_minK = right
            # Update the last seen index for maxK
            if nums[right] == maxK:
                last_maxK = right

            # A subarray ending at 'right' is fixed-bound if the most recent minK and maxK
            # are within the current valid window (defined by left_bound).
            # The number of valid start indices for such subarrays is
            # min(last_minK, last_maxK) - left_bound.
            # We add max(0, ...) to handle cases where min(last_minK, last_maxK) < left_bound,
            # meaning no valid fixed-bound subarray ends at 'right'.
            count += max(0, min(last_minK, last_maxK) - left_bound)

        return count
