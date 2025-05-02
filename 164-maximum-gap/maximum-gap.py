class Solution:
    def maximumGap(self, nums):
        n=len(nums)
        if n<2: return 0
        lo,hi=min(nums),max(nums)
        if lo==hi: return 0
        b=max(1,(hi-lo+n-2)//(n-1))
        m=(hi-lo)//b+1
        mi=[hi+1]*m; ma=[lo-1]*m
        for x in nums:
            i=(x-lo)//b
            mi[i]=x if x<mi[i] else mi[i]
            ma[i]=x if x>ma[i] else ma[i]
        ans=0; prev=lo
        for i in range(m):
            if mi[i]>hi: continue
            ans=max(ans, mi[i]-prev)
            prev=ma[i]
        return ans
