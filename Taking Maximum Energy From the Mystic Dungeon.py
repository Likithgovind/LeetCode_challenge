class Solution(object):
    def maximumEnergy(self, energy, k):
        n = len(energy)
        for t in range(n - 1, k - 1, -1):
            energy[t - k] += energy[t]
        return max(energy)
