class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        maxNum = -1
        for i in range(len(A) - 2):
            maxNum = max(A[i], maxNum)
            if (maxNum > A[i + 2]): return False
        return True