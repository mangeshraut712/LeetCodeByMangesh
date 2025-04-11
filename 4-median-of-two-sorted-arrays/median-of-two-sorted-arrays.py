import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            # Ensure nums1 is the shorter array for binary search efficiency
            nums1, nums2, m, n = nums2, nums1, n, m 

        low, high = 0, m
        total_length = m + n
        half_len = (total_length + 1) // 2

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = half_len - partition1

            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Correct partition found
                if total_length % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                # Partition1 is too large, move left in nums1
                high = partition1 - 1
            else:  # maxLeft2 > minRight1
                # Partition1 is too small, move right in nums1
                low = partition1 + 1
        
        # Should not be reached if inputs are valid sorted arrays
        return 0.0 