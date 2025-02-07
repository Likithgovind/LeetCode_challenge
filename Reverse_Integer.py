class Solution(object):
    def reverse(self, x):
        num=0
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        while x>0:
            a=x%10
            num=num*10+a
            x=x//10
            if num>2**31-1:
                return 0
        return num*sign
x=123
ans=Solution()
print(ans.reverse(x))
