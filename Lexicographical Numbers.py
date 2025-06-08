class Solution(object):
    def lexicalOrder(self, n):
        l = []
        for i in range(1, n + 1):
            l.append(str(i))
        l.sort()
        l = [int(x) for x in l]
        return l
