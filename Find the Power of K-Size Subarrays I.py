class Solution(object):
    def resultsArray(self, nums, k):
        x=[]
        for i in range(len(nums)):
            a = nums[i:i+k]
            if len(a) == k:
                l = True
                for j in range(1, len(a)):
                    if a[j] != a[j-1] + 1:
                        l = False
                        break
                if l:
                    x.append(max(a))
                else:
                    x.append(-1)
        return x
