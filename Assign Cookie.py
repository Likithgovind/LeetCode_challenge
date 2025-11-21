class Solution(object):
    def findContentChildren(self, g, s):
        s.sort()
        g.sort()
        c=0
        i=0
        j=0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]: 
                c+=1
                j+=1
                i+=1
            else:
                j+=1
        return c
