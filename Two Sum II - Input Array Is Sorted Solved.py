class Solution(object):
    def twoSum(self, numbers, target):
        n=len(numbers)
        left=0
        right=n-1
        l=[]
        while left<right:
            if numbers[left]+numbers[right]==target:
                l.append(left+1)
                l.append(right+1)
                break
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1
        return l
