class Solution(object):
    def countGood(self, nums, k):
        left=0
        count=0
        n=len(nums)
        dic={}
        pairs=0
        for right in range(n):
            num=nums[right]
            if num in dic:
                pairs+=dic[num]
                dic[num]+=1
            else:
                dic[num]=1
            while pairs >= k:
                count += (n - right)  
                dic[nums[left]] -= 1
                pairs -= dic[nums[left]]
                left += 1
        return count
