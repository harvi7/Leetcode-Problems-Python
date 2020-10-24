class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            rotations_a = rotations_b = 0
            for i in range(n):
                if A[i] != x and B[i] != x:
                    return -1
                elif A[i] != x:
                    rotations_a += 1 
                elif B[i] != x:
                    rotations_b += 1
            return min(rotations_a, rotations_b)
    
        n = len(A)
        rotations = check(A[0]) 
        if rotations != -1 or A[0] == B[0]:
            return rotations 
        else:
            return check(B[0])