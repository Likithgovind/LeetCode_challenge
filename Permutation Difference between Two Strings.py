class Solution(object):
    def findPermutationDifference(self, s, t):
        tot=0
        for i in s:
            if i in t:
                tot+=abs(s.index(i)-t.index(i))
        return tot
