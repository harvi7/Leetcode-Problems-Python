class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        
        maxRowVals = [0] * n
        maxColVals = [0] * n
        
        for i in range(n):
            for j in range(n):
                maxRowVals[i] = max(maxRowVals[i], grid[i][j])
                maxColVals[j] = max(maxColVals[j], grid[i][j])
        
        for i in range(n):
            for j in range(n):
                result += min(maxRowVals[i], maxColVals[j]) - grid[i][j]
        return result;