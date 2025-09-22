class Solution(object):
    def maxFrequencyElements(self, nums):
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        a=max(dic.values())
        c=0
        for key,values in dic.items():
            if values==a:
                c+=a
        return c
