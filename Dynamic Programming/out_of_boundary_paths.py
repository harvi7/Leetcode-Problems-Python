class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        M = 1000000000 + 7;
        dp = [[0] * n for _ in range(m)]
        dp[i][j], count = 1, 0
        for moves in range(1, N + 1):
            temp = [[0] * n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    if x == m - 1:
                        count = (count + dp[x][y]) % M
                    if y == n - 1:
                        count = (count + dp[x][y]) % M
                    if (x == 0):
                        count = (count + dp[x][y]) % M
                    if (y == 0):
                        count = (count + dp[x][y]) % M
                    temp[x][y] = (((dp[x - 1][y] if x > 0 else 0) + (dp[x + 1][y] if x < m - 1 else 0)) % M + ((dp[x][y - 1] if y > 0 else 0) + (dp[x][y + 1] if y < n - 1 else 0)) % M) % M
            dp = temp
        return count