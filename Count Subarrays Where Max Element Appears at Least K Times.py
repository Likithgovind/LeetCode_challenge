class Solution(object):
    def countSubarrays(self, nums, k):
        res=0
        l=0
        m=max(nums)
        count=0
        for r in range(len(nums)):
            if nums[r]==m:
                count+=1
            while count>=k:
                if nums[l]==m:
                    count-=1
                l+=1
            res+=l
        return res
