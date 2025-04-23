class Solution(object):
    def countLargestGroup(self, n):
        l=[]
        count=0
        length=0
        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            while len(l) <= digit_sum:
                l.append([])
            l[digit_sum].append(i)
        for s in l:
            if len(s)>length:
                length=len(s)
        for s in l:
            if len(s)==length:
                count+=1
        return count
