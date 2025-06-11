class Solution(object):
    def firstUniqChar(self, s):
        dic={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for key,values in enumerate(s):
            if dic[values]==1:
                return key
        return -1
