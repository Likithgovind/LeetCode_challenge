class Solution(object):
    def numberOfMatches(self, n):
        count=0
        while n>1:
            a=n//2
            x=n-a
            count+=a
            n=x
        return count
