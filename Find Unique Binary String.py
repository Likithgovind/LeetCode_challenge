class Solution(object):
    def findDifferentBinaryString(self, nums):
        a=[]
        for i in range(0,len(nums)):
            if nums[i][i]=="0":
                a.append('1')
            else:
                a.append('0')
        b="".join(a)
        return b
nums=["01","10"]
ans=Solution()
print(ans.findDifferentBinaryString(nums))     #output : 11
