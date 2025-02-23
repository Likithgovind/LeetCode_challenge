class Solution(object):
    def reverseWords(self, s):
        a=s.strip().split()
        l=[]
        for i in range(1,len(a)+1):
            l.append(a[-i])
        b=" ".join(l)
        return b
s = "the sky is blue"
ans=Solution()
result=ans.reverseWords(s)
print(result) #output : "blue is sky the"        
