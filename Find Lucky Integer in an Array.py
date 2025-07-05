class Solution(object):
    def findLucky(self, arr):
        dic={}
        l=[]
        for i in arr:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for key, values in dic.items():
            if key==values:
                l.append(key)
        if len(l)==0:
            return -1
        return max(l)
