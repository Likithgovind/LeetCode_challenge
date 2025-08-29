class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        l=[]
        for i in nums1:
            for j in range(len(nums2)):
                if i==nums2[j]:
                    for k in range(j+1,len(nums2)):
                        if nums2[k]>i:
                            l.append(nums2[k])
                            break
                    else:
                        l.append(-1)
        return l
