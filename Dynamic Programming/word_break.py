class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        maxLen = 0
        for word in wordDict:
            maxLen = max(maxLen, len(word))
        dp[0] = True
        for end in range(1, len(s) + 1):
            for j in range(end - 1, -1, -1):
                if end - j > maxLen: continue
                if dp[j] and s[j:end] in wordDict:
                    dp[end] = True
                    break
        return dp[len(s)]