class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= upper:
                count += (right - left)
                left += 1
            else:
                right -= 1
        upper_count = count
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] <= lower - 1:
                count += (right - left)
                left += 1
            else:
                right -= 1
        result = upper_count - count
        return result
