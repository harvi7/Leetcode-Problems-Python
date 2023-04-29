class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        rows = [i for i in range(r) for j in range(c) if grid[i][j]]
        cols = [j for j in range(c) for i in range(r) if grid[i][j]]
        
        def minDistance1D(points):
            distance = 0
            i, j = 0, len(points) - 1
            while i < j:
                distance += points[j] - points[i]
                i, j = i + 1, j - 1
            return distance
        
        return minDistance1D(rows) + minDistance1D(cols);
        
        