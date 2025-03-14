class Solution(object):
    def longestPalindrome(self, s):
        palindrome=set()
        for i in range(len(s)):
            left,right=i,i
            while left>=0 and right<len(s) and s[right]==s[left]:
                palindrome.add(s[left:right+1])
                left-=1
                right+=1
            left,right=i,i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome.add(s[left:right+1])
                left-=1
                right+=1
        longest=max(palindrome,key=len)
        return longest
s="babad"
result=Solution()
print(result.longestPalindrome(s))   #output: bab
