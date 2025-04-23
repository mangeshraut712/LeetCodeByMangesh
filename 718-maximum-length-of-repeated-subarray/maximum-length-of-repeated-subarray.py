from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [0] * (m + 1)
        max_length = 0

        for i in range(1, n + 1):
            new_dp = [0] * (m + 1)
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    new_dp[j] = dp[j - 1] + 1
                    max_length = max(max_length, new_dp[j])
            dp = new_dp

        return max_length
