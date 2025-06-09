class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        v=list(magazine)
        l=list(ransomNote)
        for i in l:
            if i not in  v:
                return False
                break
            if i in v:
                v.remove(i)
        return True
