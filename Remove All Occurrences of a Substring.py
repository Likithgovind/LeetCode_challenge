class Solution(object):
    def removeOccurrences(self, s, part):
        stack1=[]
        stack2=[]
        for char in part:
            stack2.append(char)
        for char in s:
            stack1.append(char)
            if stack1[-len(part):] == stack2:
                for _ in range(len(part)):  
                    stack1.pop()
        result="".join(stack1)
        return result
s = "daabcbaabcbc"
part="abc"
sol1=Solution()

print(sol1.removeOccurrences(s,part))
