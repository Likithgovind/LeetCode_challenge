class Solution(object):
    def addBinary(self, a, b):
        result=bin(int(a,2)+int(b,2))[2:]
        return result
