class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n, sol = len(matrix), len(matrix[0]), []
        row, col = 0, 0
        
        for i in range(m * n):
            sol.append(matrix[row][col])
            if (row + col) % 2 == 0:             
                if col == n - 1:
                    row += 1           
                elif row == 0:
                    col += 1       
                else:
                    row -= 1
                    col += 1           
            else:                           
                if row == m - 1:
                    col += 1           
                elif col == 0:
                    row += 1        
                else:
                    row += 1
                    col -= 1          
        return sol