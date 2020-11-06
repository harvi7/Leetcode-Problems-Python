class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        return sum([mat[i][i] + mat[i][N - 1 - i] for i in range(N)]) - (mat[N // 2][N // 2] if N & 1 else 0)