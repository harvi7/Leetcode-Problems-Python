class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1, area2 = (C - A) * (D - B), (G - E) * (H - F)   
        overlap = 0
        if not (E > C or G < A or F > D or H < B):
            overlap = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        return area1 + area2 - overlap
    