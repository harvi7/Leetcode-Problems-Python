class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxsqlen = 0
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0]) 
            dp = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
            for i in range(1, rows + 1):
                for j in range(1, cols + 1):
                    if matrix[i - 1][j - 1] == '1':
                        dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                        maxsqlen = max(maxsqlen, dp[i][j])

        return maxsqlen * maxsqlen