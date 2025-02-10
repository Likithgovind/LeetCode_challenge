class Solution(object):
    def singleNumber(self, nums):
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for key,value in dic.items():
            if value==1:
                return key
nums=[2,2,1]
ans=Solution()
print(ans.singleNumber(nums))
