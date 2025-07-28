class Solution(object):
    def countMaxOrSubsets(self, nums):
        c=0
        count=0
        for i in nums:
            c|=i
        for i in range(1,1<<len(nums)):
            s=[]
            for j in range(len(nums)):
                if (i &(1<<j))!=0:
                    s.append(nums[j])
            o=0
            for k in s:
                o|=k
            if o==c:
                count+=1
        return count
