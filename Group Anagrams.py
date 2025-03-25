class Solution:
    def groupAnagrams(self, strs):
        dic={}
        l=[]
        for i in strs:
            key="".join(sorted(i))
            if key not in dic:
                dic[key]=[i]
            else:
                dic[key].append(i)
        for key,values in dic.items():
            l.append(values)
        return l
strs=["eat","tea","tan","ate","nat","bat"]
result=Solution()
print(result.groupAnagrams(strs)) #Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
