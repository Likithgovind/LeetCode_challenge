class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        count=0
        for i in range(len(nums)):
            if i-k >=0 and nums[i] <=nums[i-k]:
                continue
            if i+k <len(nums) and nums[i] <=nums[i + k]:
                continue
            count+=nums[i]
        return count
