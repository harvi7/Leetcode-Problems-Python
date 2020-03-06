class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0: return 0
        result = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range (len(matrix) + 1)]
        
        max_len = 0
        for i in range(1, len(result)):
            for j in range(1, len(result[0])):
                result[i][j] = 0 if matrix[i - 1][j - 1] == '0' else (min(result[i - 1][j - 1], 
                                                                           result[i][j - 1], 
                                                                           result[i - 1][j]) + 1)
                max_len = max(result[i][j], max_len)
        return max_len * max_len