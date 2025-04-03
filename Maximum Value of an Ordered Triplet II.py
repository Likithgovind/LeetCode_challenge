class Solution(object):
    def maximumTripletValue(self, nums):
        n=len(nums)
        pre=[0]*n
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i]=max(pre[i-1],nums[i])
        suf=[0]*n
        suf[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suf[i]=max(suf[i+1],nums[i])
        triplet=0
        for j in range(1,len(nums)-1):
            i = pre[j - 1] 
            k = suf[j + 1]
            triplet=max(triplet,(i-nums[j])*k)
        return triplet
nums = [12,6,1,2,7]
result=Solution()
print(result.maximumTripletValue(nums))
