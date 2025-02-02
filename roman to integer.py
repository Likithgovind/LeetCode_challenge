class Solution(object):
    def romanToInt(self, s):
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        value=0
        total=0
        for i in reversed(s):
            current=roman[i]
            if current>=value:
                total+=current
            else:
                total-=current
            value=current
        return total
s="III"
ans=Solution()
result=ans.romanToInt(s)
print(result)
