class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        if k >= n / 2:
            maxPro = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    maxPro += prices[i] - prices[i - 1]
            return maxPro
    
        dp = [[0 for _ in range(n)] for _ in range(k + 1)]
        for i in range(1, k + 1):
            localMax = dp[i - 1][0] - prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1],  prices[j] + localMax)
                localMax = max(localMax, dp[i - 1][j] - prices[j])
        return dp[k][n-1]