class Solution(object):
    def plusOne(self, digits):
        add=""
        l=[]
        for i in digits:
            add=add+str(i)
        sum=int(add)+1
        for i in str(sum):
            l.append(int(i))
        return l
digits=[1,2,3]
ans=Solution()
result=ans.plusOne(digits)
print(result)          #output : [1,2,4]
