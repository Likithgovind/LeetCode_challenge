class Solution(object):
    def isHappy(self, n):
        if n==1 or n==7:
            return True
        elif n<10:
            return False
        while n>=10:
            count=0
            for i in str(n):
                count+=int(i)*int(i)
            n=count
        if n==1 or n==7:
            return True
        return False


n=19
result=Solution()
print(result.isHappy(n))
