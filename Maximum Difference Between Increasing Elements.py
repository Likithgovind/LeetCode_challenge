class Solution(object):
    def maximumDifference(self, nums):
        l=0
        d=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]<nums[j]:
                    a=nums[j]-nums[i]
                    d=max(d,a)
        if d==0:
            return -1
        return d
        
