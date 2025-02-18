class Solution(object):
    def isPalindrome(self, s):
        s1=""
        for i in s.lower():
            if i.isalnum():
                s1+=i
        new=s1[::-1]
        if s1==new:
            return True
        return False

s="A man, a plan, a canal: Panama"
ans=Solution()
result=ans.isPalindrome(s)
print(result)      #output : true
        
