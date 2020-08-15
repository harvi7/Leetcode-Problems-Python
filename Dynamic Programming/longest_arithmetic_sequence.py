class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        maxValue = 1;
        for i in range(len(A)):
            for j in range(0, i):
                dp[i, A[i] - A[j]] = dp.get((j, A[i] - A[j]), 0) + 1
                maxValue = max(maxValue, dp[i, A[i] - A[j]])
        return maxValue + 1