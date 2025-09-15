class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        l=text.split()
        c=0
        for i in l:
            for j in brokenLetters:
                if j in i:
                    break
            else:
                c+=1
        return c
