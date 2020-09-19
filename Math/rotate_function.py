class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        allSum, length, F = 0, len(A), 0
        for i in range(length):
            F += i * A[i]
            allSum += A[i]

        maxF = F
        for i in range(length - 1, 0, -1):
            F += allSum - length * A[i]
            maxF = max(F, maxF)
            
        return maxF 