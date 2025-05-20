class Solution(object):
    def isZeroArray(self, nums, queries):
        n = len(nums)
        times = [0] * (n + 1)
        for l, r in queries:
            times[l] += 1
            if r + 1 < len(times):
                times[r + 1] -= 1
        for i in range(1, n):
            times[i] += times[i - 1]
        for i in range(n):
            if times[i] < nums[i]:
                return False
        return True
