class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                if i - dic[nums[i]] <= k:
                    return True
                    break
            dic[nums[i]] = i
        else:
            return False
