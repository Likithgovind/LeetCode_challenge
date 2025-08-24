class Solution(object):
    def findOcurrences(self, text, first, second):
        a=text.split()
        i=0
        l=[]
        while i<len(a)-2:
            if a[i]==first and a[i+1]==second:
                l.append(a[i+2])
                i+=1
            else:
                i+=1
        return l
