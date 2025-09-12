class Solution(object):
    def doesAliceWin(self, s):
        x=0
        for i in s:
            if i in "aeiou":
                x+=1
        if x>=1:
            return True
        return False
