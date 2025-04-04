class Solution(object):
    def searchRange(self, nums, target):
        left,right=0,len(nums)-1
        first=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                first=mid
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        left,right=0,len(nums)-1
        last=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                last=mid
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return [first,last]
nums = [5,7,7,8,8,10]
target = 8
result=Solution()
print(result.searchRange(nums, target))
