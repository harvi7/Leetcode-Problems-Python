class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        m = len(matrix)
        if m == 0: return res
        n = len(matrix[0])
        
        pacific, atlantic = [[False for _ in range(n)] for _ in range(m)], [[False for _ in range(n)] for _ in range(m)]
        
        for col in range(n):
            self.dfs(matrix, 0, col, pacific, matrix[0][col])
            self.dfs(matrix, m - 1, col, atlantic, matrix[m - 1][col])

        for row in range(m):
            self.dfs(matrix, row, 0, pacific, matrix[row][0])
            self.dfs(matrix, row, n - 1, atlantic, matrix[row][n - 1])
        
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])       
        return res
    
    def dfs(self, matrix, r, c, ocean, preHeight):
        if r > len(matrix) - 1 or r < 0 or c > len(matrix[0]) - 1 or c < 0 or matrix[r][c] < preHeight or ocean[r][c]: return
        
        ocean[r][c] = True
        self.dfs(matrix, r, c + 1, ocean, matrix[r][c]);
        self.dfs(matrix, r, c - 1, ocean, matrix[r][c]);
        self.dfs(matrix, r - 1, c, ocean, matrix[r][c]);
        self.dfs(matrix, r + 1, c, ocean, matrix[r][c]);