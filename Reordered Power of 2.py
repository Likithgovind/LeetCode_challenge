class Solution(object):
    def reorderedPowerOf2(self, n):
        a=set()
        x=1
        while x<=10**9:
            a.add(''.join(sorted(str(x))))
            x*=2
        return ''.join(sorted(str(n))) in a
