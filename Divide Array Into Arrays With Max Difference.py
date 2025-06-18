class Solution(object):
    def divideArray(self, nums, k):
        l=[]
        nums.sort()
        for i in range(0,len(nums),3):
            a,b,c=nums[i],nums[i+1],nums[i+2]
            if c-a>k:
                return []
            l.append([a,b,c])
        return l
