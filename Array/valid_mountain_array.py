class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i = 0
        while i + 1 < len(A) and A[i] < A[i + 1]:
            i += 1
        
        if i == 0 or i + 1 >= len(A): return False
        
        while i + 1 < len(A):
            if A[i] <= A[i + 1]: 
                return False
            i += 1
        return True