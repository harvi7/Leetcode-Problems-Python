class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        S = -1
        A.sort()
        lo, hi = 0, len(A) -1
        while lo < hi:
            if (A[lo] + A[hi] < K):
                S = max(S, A[lo] + A[hi])
                lo += 1
            else:
                hi -= 1
        return S