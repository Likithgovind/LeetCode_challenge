class Solution(object):
    def containsDuplicate(self, nums):
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else: 
                dic[i]+=1
        for key,values in dic.items():
            if values>=2:
                return True
                break
        return False
nums=[1,2,3,1]
result=Solution()
print(result.containsDuplicate(nums))
        
