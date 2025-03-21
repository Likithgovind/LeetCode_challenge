class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char=set()
        left=0
        length=0
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left+=1
            char.add(s[right])
            length=max(length,right-left+1)
        return length
s="abcabcbb"
result=Solution()
print(result.lengthOfLongestSubstring(s)) #output: 3
