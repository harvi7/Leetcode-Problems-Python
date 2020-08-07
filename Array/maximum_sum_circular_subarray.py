class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        maxStraightSum, minStraightSum, arraySum, tempMaxSum, tempMinSum = -math.inf, math.inf, 0, 0, 0
        for i in range(len(A)):
            arraySum += A[i]          
            tempMaxSum += A[i]
            maxStraightSum = tempMaxSum if maxStraightSum < tempMaxSum else maxStraightSum
            tempMaxSum = 0 if tempMaxSum < 0 else tempMaxSum
            
            tempMinSum += A[i]
            minStraightSum = tempMinSum if minStraightSum > tempMinSum else minStraightSum
            tempMinSum = 0 if tempMinSum > 0 else tempMinSum
                
        if arraySum == minStraightSum:
            return maxStraightSum
        return max(maxStraightSum, (arraySum - minStraightSum))