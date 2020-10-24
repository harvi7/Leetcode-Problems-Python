class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if len(maze) == 0 or len(maze[0]) == 0:
            return False
        visited = dict()
        return self.DFS(maze, start, destination, visited)
    
    def DFS(self, maze, start, destination, visited):
        if start == destination:
            return True
        
        if (start[0], start[1]) in visited:
            return False
        visited[(start[0], start[1])] = 1
        
        up, down = start[0] - 1, start[0] + 1
        left, right = start[1] -1, start[1] +1
        
        while up >= 0 and maze[up][start[1]] == 0:
            up -= 1
        if self.DFS(maze, [up + 1, start[1]], destination, visited):
            return True
        
        while down < len(maze) and maze[down][start[1]] == 0:
            down += 1
        if self.DFS(maze, [down - 1, start[1]], destination, visited):
            return True
        
        while left >= 0 and maze[start[0] ][left] == 0:
            left -= 1
        if self.DFS(maze, [start[0], left + 1], destination, visited):
            return True
        
        while right < len(maze[0]) and maze[start[0] ][right] == 0:
            right += 1
        if self.DFS(maze, [start[0], right - 1], destination, visited):
            return True