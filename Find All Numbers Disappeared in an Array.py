class Solution(object):
    def findDisappearedNumbers(self, nums):
        dic={}
        l=[]
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in range(1,len(nums)+1):
            if i not in dic:
                l.append(i)
        return l
