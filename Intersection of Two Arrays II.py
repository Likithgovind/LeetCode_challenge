class Solution(object):
    def intersect(self, nums1, nums2):
        i=0
        j=0
        s1=sorted(nums1)
        s2=sorted(nums2)
        l=[]
        while i <len(s1) and j<len(s2):
            if s1[i]<s2[j]:
                i+=1
            elif s1[i]>s2[j]:
                j+=1
            else:
                l.append(s1[i])
                i+=1
                j+=1
        return l
