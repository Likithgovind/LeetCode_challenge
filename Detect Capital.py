class Solution(object):
    def detectCapitalUse(self, word):
        a=0
        b=0
        for i in word:
            if 65<=ord(i)<=90:
                a+=1
            if 97<=ord(i)<=122:
                b+=1
        if a==1 and b==len(word)-1:
            if word[0].isupper():
                return True
        if a==0 and b==len(word):
            return True
        if a==len(word) and b==0:
            return True
        else:
            return False
