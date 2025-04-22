class Solution(object):
    def mergeAlternately(self, word1, word2):
        l=0
        a=[]
        d=abs(len(word1)-len(word2))
        if len(word1)<len(word2):
            word1 += '0'*d
        else:
            word2+='0'*d
        while l<len(word1):
            a.append(word1[l])
            a.append(word2[l])
            l+=1
        for i in a:
            if i==str(0):
                a.remove(i)
        return "".join(a)
