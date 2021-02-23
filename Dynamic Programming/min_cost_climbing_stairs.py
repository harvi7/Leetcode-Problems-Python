class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1, step2 = 0, 0
        for i in range(len(cost)- 1, -1, -1):
            currentStep = cost[i] + min(step1, step2)
            step1, step2 = step2, currentStep
        
        return min(step1, step2)