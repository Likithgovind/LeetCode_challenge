class Solution(object):
    def setZeroes(self, matrix):
        n=0
        l=set()
        m=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    l.add(i)
                    m.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in l or j in m:
                    matrix[i][j]=0
        return matrix
