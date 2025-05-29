class Solution(object):
    def simplifyPath(self, path):
        part=path.split("/")
        l=[]
        if not part:
            return ""
        for i in part:
            if i=="" or i==".":
                continue
            elif i==".." :
                if l:
                    l.pop()
            else:
                l.append(i)
        return "/"+"/".join(l)
