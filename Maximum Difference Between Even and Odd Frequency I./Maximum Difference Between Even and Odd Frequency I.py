class Solution(object):
    def maxDifference(self, s):
        dic={}
        o=[]
        e=[]
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for values in dic.values():
            if values%2!=0:
                o.append(values)
            else:
                e.append(values)
        o_m=max(o)
        e_m=min(e)
        return o_m-e_m
