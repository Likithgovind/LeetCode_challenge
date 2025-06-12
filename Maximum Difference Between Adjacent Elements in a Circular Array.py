class Solution(object):
    def maxAdjacentDistance(self, nums):
        d=abs(nums[-1]-nums[0])
        for i in range(1,len(nums)):
            d=max(d,abs(nums[i]-nums[i-1]))
        return d
