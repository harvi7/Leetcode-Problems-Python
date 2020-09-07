class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or len(matrix) == 0:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        res = 0
        for i in range(rows):
            for j in range(cols):
                if dp[i][j] == 0:
                    self.dfs(matrix, i, j, dp, float("-inf"))
                    res = max(res, dp[i][j])
        return res

    
    def dfs(self, matrix, row, col, dp, prev):
        if row > len(matrix) - 1 or row < 0 or col > len(matrix[0]) - 1 or col < 0 or matrix[row][col] <= prev:
            return 0
        if dp[row][col] != 0:
            return dp[row][col]

        left = self.dfs(matrix, row, col - 1, dp, matrix[row][col]);
        right = self.dfs(matrix, row, col + 1, dp, matrix[row][col]);
        up = self.dfs(matrix, row - 1, col, dp, matrix[row][col]);
        down = self.dfs(matrix, row + 1, col, dp, matrix[row][col]);

        dp[row][col] = max(left, right, up, down) + 1
        return dp[row][col]