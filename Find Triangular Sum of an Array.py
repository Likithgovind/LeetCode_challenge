class Solution(object):
    def triangularSum(self, nums):
        if len(nums)==1:
            return nums[0]
        while len(nums)>1:
            a=[]
            for i in range(1,len(nums)):
                a.append(nums[i-1]+nums[i])
            nums=a
        x=0
        for i in nums:
            s=str(i)
            if len(s)>1:
                x=s[-1]
            else:
                x=nums[0]
        return int(x)
