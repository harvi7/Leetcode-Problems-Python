class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    cur = board[i][j]
                    if ("row " + str(i), cur) in seen or ("column " + str(j), cur) in seen or ("box " + str(i // 3) + str(j // 3), cur) in seen:
                        return False
                    seen.add(("row " + str(i), cur))
                    seen.add(("column " + str(j), cur))
                    seen.add(("box " + str(i // 3) + str(j // 3), cur))
        return True