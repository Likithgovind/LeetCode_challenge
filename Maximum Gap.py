class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2:
            return 0
        nums.sort()
        l=0
        for i in range(1,len(nums)):
            a=nums[i]-nums[i-1]
            l=max(l,a)
        return l
