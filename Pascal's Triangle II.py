class Solution(object):
    def getRow(self, rowIndex):
        l=[[1],[1,1]]
        for i in range(rowIndex):
            y=l[-1]
            x=[]
            for j in range(len(y)):
                if j==0:
                    x.append(y[j])
                if j==len(y)-1:
                    x.append(y[j])
                else:
                    z=y[j]+y[j+1]
                    x.append(z)
            l.append(x)
        return l[rowIndex]
