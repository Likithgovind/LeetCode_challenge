class Solution(object):
    def singleNumber(self, nums):
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for keys,values in dic.items():
            if values==1:
                return keys
