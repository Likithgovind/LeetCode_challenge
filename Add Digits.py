class Solution(object):
    def addDigits(self, num):
        if num<=0:
            return 0
        while num>9:
            count=0
            while num>0:
                a=num%10
                count+=a
                num=num//10
            num=count
        return num
