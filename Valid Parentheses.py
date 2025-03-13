class Solution(object):
    def isValid(self, s):
        l=[]
        dic={')':'(','}':'{',']':'['}
        for i in s:
            if i in "{[(":
                l.append(i)
            elif i in "})]":
                if l and l[-1]==dic[i]:
                    l.pop()
                else:
                    return False
                    break
        if len(l)==0:
            return True
        return False
s="()"
result=Solution()
print(result.isValid(s))  # output : true
