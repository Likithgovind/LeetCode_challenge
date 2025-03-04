class Solution(object):
    def checkPowersOfThree(self, n):
        while n > 0:
            remainder = n % 3
            if remainder == 2:
                return False
            n //= 3  
        return True
n=12
result=Solution()
print(result.checkPowersOfThree(n)) output: true
