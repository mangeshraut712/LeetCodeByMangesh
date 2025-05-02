class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        # Algorithm: Binary Search 
        ###
        nums.sort()
        count = 0

        for i in range(len(nums) - 1):
            # Find the range of indices that work with nums[i]
            left  = bisect_left(nums, lower - nums[i], i + 1)
            right = bisect_right(nums, upper - nums[i], i + 1)
            count += right - left

        return count


        # Algorithm: Two Pointers
        ###
        nums.sort()

        # Helper function to count pairs with sum <= target
        def countPairsLessThanOrEqual(target):
            count = 0
            left, right = 0, len(nums) - 1

            while left < right:
                if nums[left] + nums[right] <= target:
                    # If the sum is valid, all pairs with left fixed and 
                    # right ranging from left+1 to current right are valid
                    count += right - left
                    left  += 1
                else:
                    # If sum exceeds target, try a smaller right value
                    right -= 1

            return count

        # Count pairs in range [lower, upper] = (pairs <= upper) - (pairs <= lower-1)
        return countPairsLessThanOrEqual(upper) - countPairsLessThanOrEqual(lower - 1)