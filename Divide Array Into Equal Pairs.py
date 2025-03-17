class Solution(object):
    def divideArray(self, nums):
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for key,values in dic.items():
            if values%2!=0:
                return False
                break
        return True
nums=[3,2,3,2,2,2]
result=Solution()
print(result.divideArray(nums))  # output : true
