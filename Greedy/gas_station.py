class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currentGaining, totalGaining, candidate = 0, 0, 0
        
        for i in range(len(gas)):
            
            currentGaining += gas[i] - cost[i]
            totalGaining += gas[i] - cost[i]
            
            if currentGaining < 0:
                candidate = i + 1
                currentGaining = 0
        
        return candidate if totalGaining >= 0 else -1