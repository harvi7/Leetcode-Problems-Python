class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        ans, length = 0, len(A[0])
        for c in range(length):
            for r in range(len(A) - 1):
                if A[r][c] > A[r + 1][c]:
                    ans += 1
                    break
        return ans