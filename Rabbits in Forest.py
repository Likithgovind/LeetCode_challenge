class Solution(object):
    def numRabbits(self, answers):
        dic={}
        count=0
        v=0
        for i in answers:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in dic.keys():
            group_size = i + 1
            groups = (dic[i] + group_size - 1) // group_size
            count += groups * group_size
        return count
