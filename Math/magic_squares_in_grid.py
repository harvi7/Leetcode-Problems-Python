class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def magic(i, j):
            if grid[i + 1][j + 1] == 5 and \
            grid[i][j] + grid[i + 2][j + 2] == grid[i][j + 1] + grid[i + 2][j + 1] == grid[i][j + 2] + grid[i + 2][j] == grid[i + 1][j] + grid[i + 1][j + 2] == 10 and \
            grid[i][j + 1] + grid[i][j + 2] == grid[i + 1][j] + grid[i + 2][j] and \
            set(grid[i + di][j + dj] for di in range(3) for dj in range(3)) == s: 
                return 1
            return 0
        
        ans, R, C, s = 0, len(grid), len(grid[0]), {1,2,3,4,5,6,7,8,9}
        for r in range(R - 2):
            for c in range(C - 2):
                ans += magic(r, c)
        return ans