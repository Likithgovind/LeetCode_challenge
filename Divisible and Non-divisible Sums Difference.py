class Solution(object):
    def differenceOfSums(self, n, m):
        count1=0
        count2=0
        for i in range(1,n+1):
            if i%m==0:
                count1+=i
            else:
                count2+=i
        return count2-count1
