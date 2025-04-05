class Solution(object):
    def subsetXORSum(self, nums):
        subset=[[]]
        l=[]
        count=0
        for num in nums:
            new_subset=[]
            for s in subset:
                new_subset.append(s+[num])
            subset.extend(new_subset)
        for i in subset:
            total=0
            for j in i:
                total^=j
            l.append(total)
        for i in l:
            count+=i
        return count
