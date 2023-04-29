class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        # while len(A) >= 2:
        #     row = A.pop()            
        #     for i in range(len(row)):
        #         A[-1][i] += min(row[max(0, i - 1): min(len(row), i + 2)])
        # return min(A[0])
        dp = A[0]
        for row in A[1:]:
            dp = [value + min([dp[c], dp[max(c - 1, 0)], dp[min(len(A) - 1, c + 1)]]) for c, value in enumerate(row)]
        return min(dp)
