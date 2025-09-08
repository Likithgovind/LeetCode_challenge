class Solution(object):
    def getNoZeroIntegers(self, n):
        l=[]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i+j==n:
                    if "0" not in str(i) and "0" not in str(j):
                        l.append(i)
                        l.append(j)
                        if len(l)==2:
                            return l
                            break
