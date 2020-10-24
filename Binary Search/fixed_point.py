class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l < r:
            m = l + (r - l) // 2
            if A[m] - m < 0:
                l = m + 1
            else:
                r = m
        return l if A[l] == l else -1