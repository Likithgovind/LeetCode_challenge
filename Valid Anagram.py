class Solution(object):
    def isAnagram(self, s, t):
        dic={}
        dic1={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for j in t:
            if j not in dic1:
                dic1[j]=1
            else:
                dic1[j]+=1
        if dic==dic1:
            return True
        return False
s="anagram"
t="nagaram"
sol=Solution()
result=sol.isAnagram(s,t)
print(result)    #output : true
