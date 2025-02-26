class Solution(object):
    def maxAbsoluteSum(self, nums):
        maxsum=0
        minsum=0
        pos=0
        neg=0
        for i in range(len(nums)):
            pos+=nums[i]
            neg+=nums[i]
            if pos<0:
                pos=0
            if neg>0:
                neg=0
            maxsum=max(maxsum,pos)
            minsum=min(minsum,neg)
        return max(abs(minsum),maxsum)
nums=[1,-3,2,3,-4]
ans=Solution()
print(ans.maxAbsoluteSum(nums))
        
