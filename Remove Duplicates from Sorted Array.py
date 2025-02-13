class Solution(object):
    def removeDuplicates(self, nums):
        count=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[count]=nums[i]  
                count+=1
        return count
nums=[1,1,2]
ans=Solution()
result=ans.removeDuplicates(nums)
print(result) #output: 2
