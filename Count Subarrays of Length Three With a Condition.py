class Solution(object):
    def countSubarrays(self, nums):
        n=len(nums)
        count=0
        for i in range(n-2):
            a,b,c=nums[i],nums[i+1],nums[i+2]
            if a+c==b/2.0:
                count+=1    
        return count
