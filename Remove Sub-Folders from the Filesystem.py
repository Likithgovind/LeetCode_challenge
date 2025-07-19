class Solution(object):
    def removeSubfolders(self, folder):
        folder.sort()
        a=[folder[0]]
        for i in range(1,len(folder)):
            if not folder[i].startswith(a[-1]+"/"):
                a.append(folder[i])
        return a
