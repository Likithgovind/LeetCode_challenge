class Solution(object):
    def reverseString(self, s):
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
s=["h","e","l","l","o"]
result=Solution()
print(result.reverseString(s)) #output : ["o","l","l","e","h"]
