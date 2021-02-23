class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms and rooms[0])  
        q, dist = [(i, j) for i in range(m) for j in range(n) if not rooms[i][j]], 0
        while q:
            new = []
            dist += 1
            for row, col in q:
                for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if 0 <= r < m and 0 <= c < n and rooms[r][c] == 2147483647:
                        rooms[r][c] = dist
                        new.append((r, c))
            q = new