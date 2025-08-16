class Solution(object):
    def maximum69Number (self, num):
        if num==9999:
            return num
        l=[]
        l.append(num)
        a=str(num)
        for i in range(len(a)):
            if a[i]=="9":
                b=a[:i]+"6"+a[i+1:]
                l.append(int(b))
            if a[i]=="6":
                b=a[:i]+"9"+a[i+1:]
                l.append(int(b))
        return max(l)
