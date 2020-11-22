class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = 1 + dp[i - 1][j - 1] if A[i - 1] == B[j - 1] else max(dp[i][j - 1], dp[i - 1][j])

        return dp[m][n]