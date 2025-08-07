class Solution(object):
    def isUgly(self, n):
        a=[2,3,5]
        if n<=0:
            return False
        for i in a:
            while n%i==0:
                n=n//i
        if n==1:
            return True
        return False
