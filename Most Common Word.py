import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        para = re.sub(r'[^\w\s]', ' ', paragraph)
        p = para.lower().split()
        banned_set = set(banned)
        dic = {}
        for i in p:
            if i and i not in banned_set:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] += 1
        max_count = max(dic.values())
        for word in p:
            if word in dic and dic[word] == max_count:
                return word
