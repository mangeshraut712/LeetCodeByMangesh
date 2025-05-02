class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        top = max(nums)
        left = cnt = res = 0
        for x in nums:
            if x == top: cnt += 1
            while cnt >= k:
                if nums[left] == top: cnt -= 1
                left += 1
            res += left
        return res
