class Solution(object):
    def commonFactors(self, a, b):
        count=0
        n=min(a,b)
        for i in range(1,n+1):
            if a%i==0 and b%i==0:
                count+=1
        return count
