class Solution(object):
    def restoreString(self, s, indices):
        l=['']*len(s)
        for i in range(len(s)):
            l[indices[i]]=s[i]
        return "".join(l)
s = "codeleet"
indices = [4,5,6,7,0,1,2,3]
result=Solution()
print(result.restoreString(s,indices))     #output: leetcode
