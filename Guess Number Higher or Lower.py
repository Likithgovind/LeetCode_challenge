# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        l=1
        r=n
        while l<=r:
            m=(l+r)//2
            res=guess(m)
            if res==0:
                return m
                break
            elif res==-1:
                r=m-1
            else:
                l=m+1
