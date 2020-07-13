class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        rotten = {(i, j) for i in range(row_len) for j in range(col_len) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row_len) for j in range(col_len) if grid[i][j] == 1}
        timer = 0
        while fresh:
            if not rotten: return -1
            rotten = {(i + di, j + dj) for i, j in rotten for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i + di, j + dj) in fresh}
            fresh -= rotten
            timer += 1
        return timer