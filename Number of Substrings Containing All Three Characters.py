class Solution(object):
    def numberOfSubstrings(self, s):
        freq = {'a': 0, 'b': 0, 'c': 0} 
        left = 0 
        count = 0  
        valid_count = 0
        for right in range(len(s)):
            if s[right] in freq:
                if freq[s[right]] == 0:
                    valid_count += 1
                freq[s[right]] += 1
            while valid_count == 3:  
                count += len(s) - right  
                if s[left] in freq:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        valid_count -= 1                 
                left += 1     
        return count
s = "abcabc"
solution = Solution()
print(solution.numberOfSubstrings(s))
