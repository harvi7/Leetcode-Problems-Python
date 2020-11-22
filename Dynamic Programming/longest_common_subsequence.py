class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if (m == 0 or n == 0): return 0
        if n < m:
            return self.longestCommonSubsequence(text2, text1)
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            prevBest = 0
            for j in range(1, m + 1):
                temp = dp[j]
                dp[j] = 1 + prevBest if text1[j - 1] == text2[i - 1] else max(dp[j], dp[j - 1])
                prevBest = temp

        return dp[m]