from typing import List
from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)

        count = 0
        # Store the indices of the maximum element encountered so far
        last_max_indices = deque()

        # 'right' pointer expands the window
        for right in range(len(nums)):
            # If the current element is the maximum value
            if nums[right] == max_val:
                # Add its index to the deque
                last_max_indices.append(right)

            # If we have found at least k occurrences of the maximum element
            if len(last_max_indices) >= k:
                # The number of valid subarrays ending at 'right' is determined by
                # the position of the k-th last occurrence of max_val.
                # Any starting index from 0 up to (and including) the index of the
                # k-th last max_val will form a valid subarray ending at 'right'.
                # The index of the k-th last max_val is last_max_indices[len(last_max_indices) - k].
                # The number of possible start indices is (index of k-th last max_val) + 1.
                count += last_max_indices[len(last_max_indices) - k] + 1

        return count
