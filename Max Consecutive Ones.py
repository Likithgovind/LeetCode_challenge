class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        s=m=0
        for i in nums:
            if i!=0:
                s+=i
            else:
                s=0
            if m<s:
                m=sa
        return m
