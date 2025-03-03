class Solution(object):
    def pivotArray(self, nums, pivot):
        l1=[]
        l2=[]
        l3=[]
        for i in nums:
            if i<pivot:
                l1.append(i)
            elif i>pivot:
                l2.append(i)
            else:
                l3.append(i)
        return l1+l3+l2
nums=[9,12,5,10,14,3,10] 
pivot = 10
result=Solution()
print(result.pivotArray(nums,pivot)) #output: [9,5,3,10,10,12,14]
