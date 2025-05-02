class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        n=len(nums)
        return [sorted(range(n), key=lambda i: (nums[i][-t:], i))[k-1] for k,t in queries]
