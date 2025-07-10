class Solution(object):
    def isIsomorphic(self, s, t):
        dic1={}
        c1=0
        l1=[]
        for i in s:
            if i not in dic1:
                dic1[i]=c1
                c1+=1
            l1.append(dic1[i])
        dic2={}
        c2=0
        l2=[]
        for i in t:
            if i not in dic2:
                dic2[i]=c2
                c2+=1
            l2.append(dic2[i])
        for i in range(len(l1)):
            if l1[i]!=l2[i]:
                return False
        return True
