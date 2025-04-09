class Solution(object):
    def minOperations(self, nums, k):
        o=0
        if min(nums)<k :
            return -1
        else:
            while max(nums)>k:
                a=sorted(set(nums),reverse=True)
                h=a[1] if len(a)>1 else k
                for i in range(len(nums)):
                    if nums[i]>h:
                        nums[i]=h
                o+=1
            return o
