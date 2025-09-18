class Solution(object):
    def findSubarrays(self, nums):
        l=[]
        dic={}
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                a=nums[i:j+1]
                if len(a)==2:
                    l.append(sum(a))
        for i in l:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        d=0
        for key,values in dic.items():
            if values>=2:
                d+=1
        if d>=1:
            return True
        return False
