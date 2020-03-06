class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        minVal = A[0]
        maxVal = A[0]
        for i in range(len(A)):
            minVal = min(minVal, A[i])
            maxVal = max(maxVal, A[i])
        
        if (minVal + K >= maxVal - K):
            return 0
        else: return (maxVal - K) - (minVal + K)