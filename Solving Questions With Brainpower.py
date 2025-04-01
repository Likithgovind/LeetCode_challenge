class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * (n + 1) 
        for i in range(n - 1, -1, -1): 
            points, skip = questions[i]
            next_index = i + skip + 1
            take = points + (dp[next_index] if next_index < n else 0)
            skip = dp[i + 1]
            dp[i] = max(take, skip)
        return dp[0]
questions = [[3,2],[4,3],[4,4],[2,5]]
result = Solution()
print(result.mostPoints(questions))
