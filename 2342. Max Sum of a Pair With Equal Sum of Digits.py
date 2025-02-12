class Solution(object):
    def maximumSum(self, a):
        dic= {} 
        sum = -1  

        for num in a:
            digit = 0
            for i in str(num):  
                digit += int(i)  
            if digit in dic:
                sum = max(sum, num + dic[digit])
                dic[digit] = max(dic[digit], num)
            else:
                dic[digit] = num
        return sum
a = [18, 43, 36, 13, 7]
ans = Solution()
result = ans.maximumSum(a)
print(result)  #output: 54
