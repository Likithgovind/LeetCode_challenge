class Solution(object):
    def wordPattern(self, pattern, s):
        dic = {} 
        rev = {}  
        b = s.strip().split()
        if len(pattern) != len(b):  
            return False
        for i in range(len(pattern)):
            p = pattern[i]
            w = b[i]
            if p not in dic:
                if w in rev and rev[w] != p:  
                    return False
                dic[p] = w
                rev[w] = p
            elif dic[p] != w:  
                return False
        return True
pattern = "abba"
s = "dog cat cat dog"
ans = Solution()
print(ans.wordPattern(pattern, s))   #output: true
