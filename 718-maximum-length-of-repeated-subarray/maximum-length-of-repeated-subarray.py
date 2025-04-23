from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        # dp[i][j] is the length of the longest common subarray ending at index i-1 in nums1 and j-1 in nums2
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max_length = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
                else:
                    # If the current elements don't match, there is no common subarray
                    # ending at these indices, so the length is 0.
                    dp[i][j] = 0

        return max_length