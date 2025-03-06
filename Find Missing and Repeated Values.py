class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        dic={}
        l=[]
        nums=range(1, len(grid) * len(grid[0]) + 1)
        for i in grid:
            for j in i:
                if j not in dic:
                    dic[j]=1
                else:
                    dic[j]+=1
        for key,value in dic.items():
            if value==2:
                l.append(key)
        for i in nums:
            if i not in dic:
                l.append(i)
                break
        return l
grid=[[1,3],[2,2]]
result=Solution()
print(result.findMissingAndRepeatedValues(grid)) output: [2,4]
        
