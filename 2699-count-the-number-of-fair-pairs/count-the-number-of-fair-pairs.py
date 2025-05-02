class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        A = nums
        lo = lower - 1
        hi = upper
        n = len(A)
        ans_hi = ans_lo = 0
        l = 0; r = n - 1
        while l < r:
            s = A[l] + A[r]
            if s <= hi:
                ans_hi += r - l
                l += 1
            else:
                r -= 1
        l = 0; r = n - 1
        while l < r:
            s = A[l] + A[r]
            if s <= lo:
                ans_lo += r - l
                l += 1
            else:
                r -= 1
        return ans_hi - ans_lo
