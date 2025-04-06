class Solution(object):
    def addToArrayForm(self, num, k):
        s=""
        l=[]
        for i in num:
            s+=str(i)
        x=int(s)+k
        for i in str(x):
            l.append(int(i))
        return l
