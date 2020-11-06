class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0: return 0
#         result = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range (len(matrix) + 1)]
        
#         max_len = 0
#         for i in range(1, len(result)):
#             for j in range(1, len(result[0])):
#                 result[i][j] = 0 if matrix[i - 1][j - 1] == '0' else (min(result[i - 1][j - 1], 
#                                                                            result[i][j - 1], 
#                                                                            result[i - 1][j]) + 1)
#                 max_len = max(result[i][j], max_len)
#         return max_len * max_len
    
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        dp = [0 for _ in range(cols + 1)]
        maxsqlen, prev = 0, 0
        for i in range(1, rows + 1):
             for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                    maxsqlen = max(maxsqlen, dp[j])
                else:
                    dp[j] = 0
                prev = temp

        return maxsqlen * maxsqlen