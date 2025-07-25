class Solution(object):
    def maxSum(self, nums):
        if all(n < 0 for n in nums):
            return max(nums)
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        count=0
        for key,values in dic.items():
            if key>0:
                count+=key
        return count
