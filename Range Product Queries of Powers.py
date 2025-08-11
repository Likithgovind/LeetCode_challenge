class Solution(object):
    def productQueries(self, n, queries):
        MOD = 10**9 + 7
        x = bin(n)[2:]
        z = int(x)
        l = []
        c=1
        while z > 0:
            a = z % 10
            if a == 1:
                l.append(c)
            c *= 2
            z //= 10
        q = []
        for i in queries:
            c = 1
            for j in range(i[0], i[1] + 1):
                c = (c * l[j]) % MOD
            q.append(c)
        return q
