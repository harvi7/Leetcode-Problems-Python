class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
#         if len(A) == 0:
#             return 0
#         maxStraightSum, minStraightSum, arraySum, tempMaxSum, tempMinSum = -math.inf, math.inf, 0, 0, 0
#         for i in range(len(A)):
#             arraySum += A[i]          
#             tempMaxSum += A[i]
#             maxStraightSum = tempMaxSum if maxStraightSum < tempMaxSum else maxStraightSum
#             tempMaxSum = 0 if tempMaxSum < 0 else tempMaxSum
            
#             tempMinSum += A[i]
#             minStraightSum = tempMinSum if minStraightSum > tempMinSum else minStraightSum
#             tempMinSum = 0 if tempMinSum > 0 else tempMinSum
                
#         if arraySum == minStraightSum:
#             return maxStraightSum
#         return max(maxStraightSum, (arraySum - minStraightSum))

        total_sum = 0;
        max_ending_at = 0;
        min_ending_at = 0;
        max_sum = -math.inf
        min_sum = math.inf

        for x in A:
            total_sum += x
            
            max_ending_at = max(max_ending_at + x, x)
            max_sum = max(max_ending_at, max_sum)
            
            min_ending_at = min(min_ending_at + x, x)
            min_sum = min(min_ending_at, min_sum)
            
        if max_sum > 0:
            return max(max_sum, total_sum - min_sum)
        return max_sum