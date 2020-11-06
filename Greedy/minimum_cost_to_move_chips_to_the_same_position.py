class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even, odd = 0, 0
        for i in position:
            if i%2 == 1: odd += 1
            else: even += 1
        
        return min(odd, even)