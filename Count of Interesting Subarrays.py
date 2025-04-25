class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        count = 0
        prefix = 0
        freq = {0: 1} 
        for num in nums:
            if num % modulo == k:
                prefix += 1
            curr = prefix % modulo
            target = (curr - k + modulo) % modulo
            if target in freq:
                count += freq[target]
            if curr in freq:
                freq[curr] += 1
            else:
                freq[curr] = 1
        return count
