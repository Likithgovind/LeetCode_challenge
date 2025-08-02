class Solution(object):
    def summaryRanges(self, nums):
        l=[]
        i=0
        while i<len(nums):
            x=i
            for j in range(i+1,len(nums)):
                if nums[j]==nums[j-1]+1:
                    x=j
                else:
                    break
            if x==i:
                l.append(str(nums[i]))
            else:
                l.append(str(nums[i]) + "->" + str(nums[x]))
            i = x + 1
        return l
