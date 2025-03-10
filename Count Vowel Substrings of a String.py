class Solution(object):
    def countVowelSubstrings(self, word):
        vowel={'a','e','i','o','u'}
        count=0
        for i in range(len(word)):
            vowel_set=set()
            for j in range(i,len(word)):
                if word[j] in vowel:
                    vowel_set.add(word[j])
                    if vowel_set==vowel:
                        count+=1
                else:
                    break
        return count
word="aeiouu"
result=Solution()
print(result.countVowelSubstrings(word))
