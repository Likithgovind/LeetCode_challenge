class Solution(object):
    def reverseDegree(self, s):
        c=0
        for i in range(len(s)):
            a = ord(s[i])
            d = 97 - a + 26
            x=d*(i+1)
            c+=x
        return c
