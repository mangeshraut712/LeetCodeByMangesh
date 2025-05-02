class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        def f(t):
            cnt,l,r=0,0,len(nums)-1
            while l<r:
                if nums[l]+nums[r]<=t:
                    cnt+=r-l; l+=1
                else:
                    r-=1
            return cnt
        return f(upper)-f(lower-1)
