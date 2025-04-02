class Solution(object):
    def maximumTripletValue(self, nums):
        result=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    result=max(result,(nums[i]-nums[j])*nums[k])
        return result
nums = [12,6,1,2,7]
result=Solution()
print(result.maximumTripletValue(nums))
