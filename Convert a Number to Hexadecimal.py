class Solution(object):
    def toHex(self, num):
        bits=32
        if num<0:
            a=num & (2**bits - 1)
            return format(a,'x')
        return format(num,'x')
