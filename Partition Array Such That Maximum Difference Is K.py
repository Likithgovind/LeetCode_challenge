class Solution(object):
    def partitionArray(self, nums, k):
        nums.sort()
        count=1
        m=nums[0]
        for i in nums:
            if i-m>k:
                count+=1
                m=i
        return count
