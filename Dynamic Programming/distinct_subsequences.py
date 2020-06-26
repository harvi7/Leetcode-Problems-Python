class Solution:
    def numDistinct(self, S: str, T: str) -> int:
        sl = len(S)
        tl = len(T)
	
        dp = [[0 for i in range(sl + 1)] for j in range((tl + 1))]

        for i in range(sl + 1):
            dp[0][i] = 1

        for t in range(1, tl + 1):
            for s in range(1, sl + 1):
                dp[t][s] = dp[t][s - 1]
                if S[s - 1] == T[t - 1]:
                    dp[t][s] += dp[t - 1][s -1]

        return dp[tl][sl]