class Solution(object):
    def partitionLabels(self, s):
        l=[]
        dic={}
        for i in range(len(s)):
            dic[s[i]]=i
        st,ed=0,0
        for i in range(len(s)):
            ed=max(ed,dic[s[i]])
            if i==ed:
                l.append(ed-st+1)
                st=i+1
        return l
s="ababcbacadefegdehijhklij"
result=Solution()
print(result.partitionLabels(s))  #Output: [9,7,8]
