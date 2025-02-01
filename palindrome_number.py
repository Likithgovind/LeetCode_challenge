class Solution(object):
    def isPalindrome(self, x):
        x=str(x)

        if x[::-1]==x:
            return True
        return False
x=121
sol1=Solution()
result=sol1.isPalindrome(x)   
print(result)
