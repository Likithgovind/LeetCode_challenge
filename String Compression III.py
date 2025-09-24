class Solution(object):
    def compressedString(self, word):
        dic = {}
        s = ""
        count = 1
        for i in range(1, len(word)+1):
            if i < len(word) and word[i] == word[i-1]:
                count += 1
                if count == 10:
                    s += "9" + word[i-1]
                    count = 1
            else:
                s += str(count) + word[i-1]
                count = 1
        return s
