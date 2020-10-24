class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        start = m * n - k % (m * n)
        ans = []
        for i in range(start, m * n + start):
            j = i % (m * n)
            r, c =  j // n, j % n
            if not (j - start) % n:
                ans.append([])
            ans[-1].append(grid[r][c]) 
        return ans