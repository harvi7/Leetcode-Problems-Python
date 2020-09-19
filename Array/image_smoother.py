class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        def isValid(x, y, rows, cols):
            return x >= 0 and x < rows and y >= 0 and y < cols
            
        if not M: return None
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in range(R):
            for c in range(C):
                count = 0
                for incR in [-1, 0, 1]:
                    for incC in [-1, 0, 1]:
                        if isValid(r + incR, c + incC, R, C):
                            ans[r][c] += M[r + incR][c + incC]
                            count += 1
                ans[r][c] //= count

        return ans