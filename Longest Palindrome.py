class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return len(s)
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        e = 0
        o = 0
        for key, values in dic.items():
            if values % 2 == 0:
                e += values
            else:
                e += values - 1  
                o = 1            
        return e + o
