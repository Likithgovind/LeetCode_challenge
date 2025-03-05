class Solution(object):
    def coloredCells(self, n):
        if n==1:
            return 1
        return 2*n*(n-1)+1
n=1
result=Solution()
print(result.coloredCells(n)) output: 1
