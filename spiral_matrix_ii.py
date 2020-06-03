class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        rowBegin, rowEnd, colBegin, colEnd, counter = 0, n - 1, 0, n - 1, 1
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd + 1):
                matrix[rowBegin][i] = counter
                counter += 1
            rowBegin += 1
        
            for i in range(rowBegin, rowEnd + 1):
                matrix[i][colEnd] = counter
                counter += 1
            colEnd -= 1
    
            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    matrix[rowEnd][i] = counter
                    counter += 1
            rowEnd -= 1
            
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    matrix[i][colBegin] = counter
                    counter += 1
            colBegin += 1
        return matrix