dirs = [[0, -1], [0, 1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0: return board
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 0:
                    lives = self.count(board, i, j)
                    if lives == 3:
                        board[i][j] = -1
                if board[i][j] == 1:
                    lives = self.count(board, i ,j)
                    if lives < 2 or lives > 3:
                        board[i][j] = 2
        self.update(board)
    
    def update(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 1
                if board[i][j] == 2:
                    board[i][j] = 0
    
    def count(self, board, row, col):
        res = 0
        for direction in dirs:
            newRow = row + direction[0]
            newCol = col + direction[1]
            
            if newRow >= 0 and newRow <len(board) and newCol >= 0 and newCol < len(board[0]) and (board[newRow][newCol] == 1 or board[newRow][newCol] == 2):
                res += 1
        return res