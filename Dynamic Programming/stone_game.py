class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
 
        for i in range(n):
            for j in range(n):
                dp[i][j] = -1
        
        return self.solve(piles, dp, 0, n - 1) > 0
    
    def solve(self, piles, dp, i, j):
        if i > j: return 0
        
        if dp[i][j] != -1: return dp[i][j]
        
        dp[i][j] = max(piles[i] - self.solve(piles, dp, i + 1, j), piles[j] - self.solve(piles, dp, i, j - 1))
        return dp[i][j]