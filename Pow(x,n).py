class Solution(object):
    def myPow(self, x, n):
        x=float(x)
        n=int(n)
        pow=x**n
        return pow
x = 2.00000
n = 10
ans=Solution()
result=ans.myPow(x,n)
print(result)   #output : 1024.00000
