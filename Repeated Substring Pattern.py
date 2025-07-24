class Solution(object):
    def repeatedSubstringPattern(self, s):
        a=(s+s)[1:-1]
        return s in a
