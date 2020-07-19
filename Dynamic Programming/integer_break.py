class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1) 
        for i in range(n + 1):
            for j in range(i + 1):
                dp[i] = max(dp[i], dp[j] * (i - j), (i - j) * j)

        return dp[n]