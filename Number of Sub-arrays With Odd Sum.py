class Solution(object):
    def numOfSubarrays(self, arr):
        mod=1000000007
        odd=0
        even=1
        result=0
        sum_=0
        for i in arr:
            sum_+=i
            if sum_%2==0:
                result=(result+odd)%mod
                even+=1
            else:
                result=(result+even)%mod
                odd+=1
        return result    
arr=[1,3,5]
ans=Solution()
result=ans.numOfSubarrays(arr)
print(result)        #0utput : 4
