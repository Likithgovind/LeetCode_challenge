class Solution(object):
    def triangleType(self, nums):
        a,b,c=nums[0],nums[1],nums[2]
        if a+b<=c or a+c<=b or b+c<=a:
            return "none"
        l=len(set([a,b,c]))
        if l==1:
            return "equilateral"
        elif l==2:
            return "isosceles"
        else:
            return "scalene"
        
