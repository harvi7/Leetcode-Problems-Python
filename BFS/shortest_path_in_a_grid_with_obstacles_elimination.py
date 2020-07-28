# https://www.youtube.com/watch?v=-w9Quj5rfwA

import collections
import heapq

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def neighbors(i, j, obstacleCount):
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < rows and 0 <= y < cols:
                    newObstacleCount = obstacleCount + grid[x][y]
                    if newObstacleCount <= k and (x, y, newObstacleCount) not in visited:
                        yield x, y, newObstacleCount
 
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque([(0, 0, 0, 0)])  # steps, i, j, obstacleCount
        visited = set()
        visited.add((0, 0, 0))  # i, j, obstacleCount

        while queue:
            steps, i, j, obstacleCount = queue.popleft()
            if i == rows - 1 and j == cols - 1:
                return steps
            for x, y, oc in neighbors(i, j, obstacleCount):
                queue.append((steps + 1, x, y, oc))
                visited.add((x, y, oc))

        return -1
#         def neighbors(i, j, b):
#             for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
#                 if 0 <= x < rows and 0 <= y < cols and b + grid[x][y] <= k:
#                     yield x, y, b + grid[x][y]
 
#         rows, cols, INF = len(grid), len(grid[0]), float('inf')
#         pq = [(0, 0, 0, 0)]
#         dist = {(0, 0, 0): 0}
 
#         while pq:
#             d, i, j, b = heapq.heappop(pq)
#             if dist.get((i, j, b), INF) < d:
#                 continue
 
#             if i == rows - 1 and j == cols - 1:
#                 return d
 
#             for x, y, nb in neighbors(i, j, b):
#                 if dist.get((x, y, nb), INF) > d + 1:
#                     dist[(x, y, nb)] = d + 1
#                     heapq.heappush(pq, (d + 1, x, y, nb))
 
#         return -1