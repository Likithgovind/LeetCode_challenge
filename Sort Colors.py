class Solution(object):
    def sortColors(self, nums):
        count0 = 0
        count1 = 0
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
        for i in range(len(nums)):
            if i < count0:
                nums[i] = 0
            elif i < count0 + count1:
                nums[i] = 1
            else:
                nums[i] = 2
