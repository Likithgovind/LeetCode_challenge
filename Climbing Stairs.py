class Solution(object):
    def climbStairs(self, n):
        a=0
        b=1
        for i in range(n):
            a,b=b,a+b
        return b
n=2
result=Solution()
print(result.climbStairs(n)) #output : 2
