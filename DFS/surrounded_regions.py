class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        self.rows = len(board)
        self.cols = len(board[0])
        
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        for j in range(self.cols):
            if board[0][j] == 'O':
                self.dfs(board, 0, j, visited, False)
            if board[self.rows - 1][j] == 'O':
                self.dfs(board, self.rows - 1, j, visited, False)
        
        for i in range(self.rows):
            if board[i][0] == 'O':
                self.dfs(board, i, 0, visited, False)
            if board[i][self.cols - 1] == 'O':
                self.dfs(board, i, self.cols - 1, visited, False)
        
        for i in range(1, self.rows - 1):
            for j in range(1, self.cols - 1):
                if board[i][j] == 'O' and not visited[i][j]:
                    self.dfs(board, i, j, visited, True)
                
        
        


    def dfs(self, board, row, col, visited, flip):
        if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1: return
        if visited[row][col]: return
        if board[row][col] == 'X': return
        if flip:
            board[row][col] = 'X'
        
        visited[row][col] = True
        self.dfs(board, row + 1, col, visited, flip)
        self.dfs(board, row - 1, col, visited, flip)
        self.dfs(board, row, col + 1, visited, flip)
        self.dfs(board, row, col - 1, visited, flip)