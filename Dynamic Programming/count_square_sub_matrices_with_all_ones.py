class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        counts = [0] * m
        topleft, result = 0, 0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    top = 0 if i == 0 else counts[j]
                    left = 0 if j == 0 else counts[j - 1]
                    counts[j] = 1 + min(top, left, topleft)
                    result += counts[j]
                    
                    topleft = 0 if j == m - 1 else top
                else:
                    counts[j] = 0
        return result