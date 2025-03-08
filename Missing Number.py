class Solution(object):
    def missingNumber(self, nums):
        n=range(0,len(nums)+1)
        for i in n :
            if i not in nums:
                return i
nums=[3,0,1]
result=Solution()
print(result.missingNumber(nums))
