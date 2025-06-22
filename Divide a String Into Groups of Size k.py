class Solution(object):
    def divideString(self, s, k, fill):
        if not s:
            return []
        l=[]
        while 0<len(s):
            if len(s)%k!=0:
                s+=fill
            else:
                break
        x=0
        c=k
        while (len(s)/k)>len(l):
            l.append(s[x:c])
            c=c+k
            x=x+k
        return l
