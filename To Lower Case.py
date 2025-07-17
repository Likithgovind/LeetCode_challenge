class Solution(object):
    def toLowerCase(self, s):
        o=""
        for i in s:
            if 65<=ord(i)<=90:
                o+=chr(ord(i)+32)
            else:
                o+=i
        return o
