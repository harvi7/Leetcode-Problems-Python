class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board) == 0 or len(board[0]) == 0: return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.search(board, word, 0, i , j):
                    return True
        return False
    
    def search(self, board, word, index, i, j):
        if index == len(word): return True
        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n or word[index] != board[i][j]: return False
        c = board[i][j]
        board[i][j] = '#';
        res = self.search(board, word, index + 1, i - 1, j) or self.search(board, word, index + 1, i + 1, j) or self.search(board, word, index + 1, i, j - 1) or self.search(board, word, index + 1, i, j + 1)
        board[i][j] = c
        return res