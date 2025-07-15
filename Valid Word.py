class Solution(object):
    def isValid(self, word):
        n=list(word)
        v=[]
        c=[]
        o=['a', 'e', 'i', 'o', 'u']
        if len(word)<=2:
            return False
        for i in word:
            if i.lower() in o:
                v.append(i)
            if i.lower() not in o and i.isalpha():
                c.append(i)
        for i in n[:]:
            if 65<=ord(i)<=90 or 97<=ord(i)<=122 or 48<=ord(i)<=57:
                n.remove(i)
            else:
                return False
        else:
            if len(n)==0 and len(v) >= 1 and len(c) >= 1:
                return True
            else:
                return False
