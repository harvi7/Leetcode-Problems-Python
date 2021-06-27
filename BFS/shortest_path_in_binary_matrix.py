class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        dir = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def get_neighbours(row, col):
            for row_difference, col_difference in dir:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= m and 0 <= new_col <= n):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        if grid[0][0] != 0 or grid[m][n] != 0:
            return -1
        
        q = deque()
        q.append((0, 0))
        grid[0][0] = 1 
        
        while q:
            row, col = q.popleft()
            distance = grid[row][col]
            if (row, col) == (m, n):
                return distance
            for neighbour_row, neighbour_col in get_neighbours(row, col):
                grid[neighbour_row][neighbour_col] = distance + 1
                q.append((neighbour_row, neighbour_col))
        
        return -1