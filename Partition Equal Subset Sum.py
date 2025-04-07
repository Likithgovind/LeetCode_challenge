class Solution(object):
    def canPartition(self, nums):
        total=sum(nums)
        if total%2!=0:
            return False
        t=total//2
        st={0}
        for num in nums:
            n=set()
            for s in st:
                n.add(s+num)
            st.update(n)
        if t in st:
            return True
        return False
