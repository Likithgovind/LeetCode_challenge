class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        return -1
haystack="sadbutsad"
needle="sad"
ans=Solution()
ans.strStr(haystack,needle) #output : 0
