class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                minHp = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                if minHp < 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = minHp

        return dp[0][0]