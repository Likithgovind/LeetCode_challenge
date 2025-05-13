class Solution(object):
    def lengthAfterTransformations(self, s, t):
        MOD = 10**9 + 7
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        c = 0
        while c < t:
            new_freq = [0] * 26
            for i in range(26):
                if i == 25:
                    new_freq[0] = (new_freq[0] + freq[25]) % MOD  
                    new_freq[1] = (new_freq[1] + freq[25]) % MOD  
                else:
                    new_freq[i + 1] = (new_freq[i + 1] + freq[i]) % MOD
            freq = new_freq
            c += 1
        return sum(freq) % MOD
