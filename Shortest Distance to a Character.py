class Solution(object):
    def shortestToChar(self, s, c):
        l = []  
        a = [] 
        for i in range(len(s)):
            if s[i] == c:
                l.append(i)
        for i in range(len(s)):
            min_distance = min(abs(i - e) for e in l)
            a.append(min_distance)
        return a
