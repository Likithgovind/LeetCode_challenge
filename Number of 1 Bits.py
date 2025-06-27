class Solution(object):
    def hammingWeight(self, n):
        binary=bin(n)[2:]
        for i in str(binary):
            if i=="1":
                count+=1
        return count
        
