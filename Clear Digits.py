class Solution(object):
    def clearDigits(self, s):
        l=[]
        for char in s:
            if char.isalpha():
                l.append(char)
            elif char.isdigit() and l:
                l.pop()
                
        return "".join(l)
s = "cb34"
a="abc"
result=Solution()
print(result.clearDigits(s))   #output= ""
print(result.clearDigits(a))   #output= "abc"
