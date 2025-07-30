class Solution(object):
    def longestSubarray(self, ns):
        mx = max(ns)
        a = 0
        c = 0
        ns.append(-1)
        for n in ns:
            if n == mx:
                c += 1
            else:
                a = max(a, c)
                c = 0
        return a 
