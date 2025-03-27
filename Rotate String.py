class Solution(object):
    def rotateString(self, s, goal):
        for i in range(len(s)):
            result=s[i:]+s[:i]
            if result==goal:
                return True
        return False
s = "abcde"
goal = "cdeab"
result=Solution()
print(result.rotateString(s,goal))      #output: true
