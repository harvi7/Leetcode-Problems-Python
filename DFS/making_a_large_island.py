class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        A = [0] * (n * n + 2)
        index = 2

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    A[index] = self.dfs(grid, i, j, index)
                    index += 1

        hasZero = False
        largest = 0;
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    hasZero = True
                    area_set =set()
                    if i > 0: area_set.add(grid[i - 1][j])
                    if j > 0: area_set.add(grid[i][j - 1])
                    if i < n - 1: area_set.add(grid[i + 1][j])
                    if j < n - 1: area_set.add(grid[i][j + 1])

                    area = 1;
                    for k in area_set:
                        area += A[k]

                    largest = max(largest, area)


        return largest if hasZero else n * n

    def dfs(self, grid, x, y, color) :
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
            return 0
        grid[x][y] = color
        return 1 + self.dfs(grid, x + 1, y, color) + self.dfs(grid, x - 1, y, color) + self.dfs(grid, x, y + 1, color) + self.dfs(grid, x, y - 1, color)
