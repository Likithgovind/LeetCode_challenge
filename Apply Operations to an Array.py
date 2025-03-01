class Solution(object):
    def applyOperations(self, nums):
        l=[]
        for i in range(len(nums)-1):
            if nums[i]!=0:
                if nums[i]!=nums[i+1]:
                    l.append(nums[i])
                else:
                    b=nums[i]*2
                    l.append(b)
                    nums[i+1]=0
            else:
                l.append(0)
        if nums[-1]!=0:
            l.append(nums[-1])
        else:
            l.append(0)
        n=0
        for i in l:
            if i==n:
                l.remove(n)
                l.append(n)
        return l
nums=[1,2,2,1,1,0]
result=Solution()
print(result.applyOperations(nums))  output: [1,4,2,0,0,0]
