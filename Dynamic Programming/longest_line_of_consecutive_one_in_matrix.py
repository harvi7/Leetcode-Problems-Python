class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        n, m, ones = len(M), len(M[0]) if M else 0, 0
        dp = [[[0, 0, 0 ,0] for j in range(m + 2)] for i in range(2)]
        for i in range(n):
            for j in range(m):
                if M[i][j] == 1:
                    dp[1][j + 1][0] = dp[1][j][0] + 1
                    dp[1][j + 1][1] = dp[0][j][1] + 1
                    dp[1][j + 1][2] = dp[0][j + 1][2] + 1
                    dp[1][j + 1][3] = dp[0][j + 2][3] + 1
                    ones = max(ones, max(dp[1][j + 1]))
            dp[0], dp[1] = dp[1], dp[0]
            for j in range(1, m + 1):
                dp[1][j][:] = [0] * 4
        return ones