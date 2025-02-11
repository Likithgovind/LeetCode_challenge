class Solution(object):
    def majorityElement(self, nums):
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        max_count=max(dic.values())
        for key,value in dic.items():
            if value==max_count:
                return key
nums=[3,2,3]
ans=Solution()
print(ans.majorityElement(nums))   #output: 3
