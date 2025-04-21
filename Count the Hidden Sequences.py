class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        s = [0]
        f = 0
        for i in differences:
            a = s[f] + i
            s.append(a)
            f += 1
        n = min(s)
        m = max(s)
        min_start = lower - n
        max_start = upper - m
        result = max(0, max_start - min_start + 1)
        return result
