class Solution(object):
    def generate(self, numRows):
        l=[[1],[1,1]]
        if numRows==1:
            return [[1]]
        if numRows==2:
            return l
        for i in range(numRows-2):
            c=0
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
        return l
