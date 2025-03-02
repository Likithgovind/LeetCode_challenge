class Solution(object):
    def moveZeroes(self, nums):
        n=0
        for i in nums:
            if i==n:
                nums.remove(i)
                nums.append(i)
        return nums
nums=[0,1,0,3,12]
result=Solution()
print(result.moveZeroes(nums)) output:[1,3,12,0,0]
        
