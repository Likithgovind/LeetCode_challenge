class Solution(object):
    def lengthOfLastWord(self, s):
        word=s.strip().split()
        result=word[-1]
        return len(result)
s="Hello World"
ans=Solution()
print(ans.lengthOfLastWord(s))   #output: 5
