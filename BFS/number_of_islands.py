class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0;
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1;
                    callBFS(grid, i, j)
        return count;
    
def callBFS(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0': return    
    grid[i][j] = '0';
    callBFS(grid, i + 1, j);
    callBFS(grid, i - 1, j);
    callBFS(grid, i, j + 1);
    callBFS(grid, i, j - 1);