class Solution(object):
    def findWords(self, words):
        a="qwertyuiop"
        b="asdfghjkl"
        c="zxcvbnm"
        l=[]
        for i in words:
            if i[0].lower() in a:
                count=0
                for j in range(len(i)):
                    if i[j].lower() in a:
                        count+=1
                if count==len(i):
                    l.append(i)
            if i[0].lower() in b:
                count=0
                for j in range(len(i)):
                    if i[j].lower() in b:
                        count+=1
                if count==len(i):
                    l.append(i)
            if i[0].lower() in c:
                count=0
                for j in range(len(i)):
                    if i[j].lower() in c:
                        count+=1
                if count==len(i):
                    l.append(i)
        return l
