class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        l=[]
        r=[]
        for i in range(len(nums)):
            if nums[i]==key:
                l.append(i)
        for i in range(len(nums)):
            for j in l:
                if abs(i-j)<=k and nums[j]==key:
                    r.append(i)
                    break
        return r
