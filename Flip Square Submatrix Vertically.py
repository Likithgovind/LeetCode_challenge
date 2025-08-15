class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        sub = []
        for i in range(x, x + k):
            sub.append(grid[i][y:y + k])
        sub.reverse()
        for i in range(k):
            for j in range(k):
                grid[x + i][y + j] = sub[i][j]
        return grid
