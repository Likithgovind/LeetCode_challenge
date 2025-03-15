class Solution(object):
    def mySqrt(self, x):
        low,high=0,x
        ans=0
        while low<=high:
            mid=(low+high)//2
            if mid*mid==x:
                ans=mid
                break
            elif mid * mid < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
x=4
sol=Solution()
result=sol.mySqrt(x)
print(result)    #output:2
