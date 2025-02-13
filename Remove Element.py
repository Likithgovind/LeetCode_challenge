class Solution(object):
    def removeElement(self, nums, val):
        count=0
        for i in nums:
            if i==val:
                nums.remove(i)
                nums.append(i)
        for i in nums:
            if i!=val:
                count+=1
        return count
nums = [3,2,2,3]
val = 3
ans=Solution()
result=ans.removeElement(nums,val)
print(result)
