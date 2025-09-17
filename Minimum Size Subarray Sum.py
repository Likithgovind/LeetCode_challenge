class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        r=0
        s=0
        x=[]
        while r<len(nums):
            s+=nums[r]
            while s>=target:
                x.append(r-l+1)
                s-=nums[l]
                l+=1
            r+=1
        if len(x)==0:
            return 0
        return min(x)
