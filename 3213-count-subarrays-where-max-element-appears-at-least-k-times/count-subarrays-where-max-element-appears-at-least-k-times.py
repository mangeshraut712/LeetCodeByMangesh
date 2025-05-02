class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m, pos, ans = max(nums), [], 0
        for i, v in enumerate(nums):
            if v == m: pos.append(i)
            if len(pos) >= k: ans += pos[-k] + 1
        return ans
