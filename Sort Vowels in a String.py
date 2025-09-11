class Solution(object):
    def sortVowels(self, s):
        v = {"a","e","i","o","u","A","E","I","O","U"}
        l = []
        for i in s:
            if i in v:
                l.append(i)
        if len(l)==0:
            return s
        a = sorted(l)
        c = 0
        x = s
        for j in range(len(s)):
            if x[j] in v:
                x = x[:j] + a[c] + x[j+1:]
                c += 1
        return x
