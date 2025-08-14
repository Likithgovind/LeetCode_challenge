class Solution(object):
    def largestGoodInteger(self, num):
        q = []
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                q.append(num[i]*3)
        return max(q) if q else ""
