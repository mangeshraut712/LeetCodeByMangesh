class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0               # total valid subarrays
        top = max(nums)         # the maximum strength in all trials
        left = 0                # left boundary of our window
        window = 0              # how many times 'top' appears in the window

        for right in range(len(nums)):
            # include the new trial at `right`
            if nums[right] == top:
                window += 1
            
            # if 'top' appears k or more times, shrink from the left
            while window >= k:
                if nums[left] == top:
                    window -= 1
                left += 1
            
            # every subarray ending at `right` and starting before `left` is valid
            count += left

        return count