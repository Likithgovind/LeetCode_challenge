class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return "0"
        c=""
        if num<0:
            n=-1*num
        else:
            n=num
        while n>0:
            a=n%7
            c+=str(a)
            n=n//7
        x=c[::-1]
        if num<0:
            z=int(x)*-1
            return (str(z))
        else:
            return (x)
