class Solution(object):
    def findNumbers(self, nums):
        res=0
        for i in nums:
            count=0
            while i>0:
                num=i%10
                count+=1
                i=i//10
            if count%2==0:
                res+=1
        return res
