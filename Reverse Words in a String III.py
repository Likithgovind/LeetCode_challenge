class Solution(object):
    def reverseWords(self, s):
        a=s.split(" ")
        l=[]
        for i in a:
            l.append(i[::-1])
        return " ".join(l)
