class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results, solutions, queen_positions = [], [], set() 
        self.solveNQueensHelper(n, queen_positions, 0, solutions)

        for solution in solutions:  # construct boards from solutions list
            board = ['']*n
            for i in range(n):
                for j in range(n):
                    board[i] = board[i] + '.' if (i, j) not in solution else board[i] + 'Q'
            results.append(board)
        return results

    def solveNQueensHelper(self, n, queen_positions, column, solutions):
        if column == n:
            solutions.append(copy.copy(queen_positions))

        for row in range(n):
            if self.isSafe((row, column), queen_positions):
                queen_positions.add((row, column))  # choose
                self.solveNQueensHelper(n, queen_positions, column + 1, solutions)  # explore             
                queen_positions.remove((row, column))  # un-choose

    def isSafe(self, position, queen_positions):
        for queen in queen_positions:
            if (queen[0] == position[0] or  # same row
                    abs(queen[1] - position[1]) == abs(queen[0] - position[0])):  # same diagonal
                return False
        return True