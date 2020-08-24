class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        if rows == 0: return matrix
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != 0: matrix[i][j] = float('inf')

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != 0:
                    if i > 0 and matrix[i - 1][j] != float('inf'):
                        matrix[i][j] = min(matrix[i][j], matrix[i - 1][j] + 1)
                    if j > 0 and matrix[i][j - 1] != float('inf'):
                        matrix[i][j] = min(matrix[i][j], matrix[i][j - 1] + 1)


        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i < len(matrix) - 1 and matrix[i + 1][j] != float('inf'):
                        matrix[i][j] = min(matrix[i][j], matrix[i + 1][j] + 1)
                    if j < len(matrix[0]) - 1 and matrix[i][j + 1] != float('inf'):
                        matrix[i][j] = min(matrix[i][j], matrix[i][j + 1] + 1)
        
        return matrix