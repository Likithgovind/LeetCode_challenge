class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a = nums1 + nums2
        arr = sorted(a)
        tot = len(arr)
        if tot % 2 == 0:
            res = arr[tot//2] + arr[(tot//2)-1]
            return float(res)/2
        else:
            return arr[tot/2]
