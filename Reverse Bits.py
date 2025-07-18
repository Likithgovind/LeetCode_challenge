class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num=bin(n)[2:]
        num=num.zfill(32) 
        reverse=num[::-1] 
        val=int(reverse,2)
        return val
