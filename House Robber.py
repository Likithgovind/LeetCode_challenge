class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        pre1,pre2=0,0
        for i in nums:
            temp=pre1
            pre1=max(pre2+i,pre1)
            pre2=temp
        return pre1
nums=[1,2,3,1]
result=Solution()
print(result.rob(nums))
