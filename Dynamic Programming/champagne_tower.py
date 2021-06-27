class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r + 1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r + 1][c] += q
                    A[r + 1][c + 1] += q

        return min(1, A[query_row][query_glass])