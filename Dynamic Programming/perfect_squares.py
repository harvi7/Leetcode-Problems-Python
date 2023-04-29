class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0: return 0
        dp = [i for i in range(n + 1)]
        
        for i in range(2, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]