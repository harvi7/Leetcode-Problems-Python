class Solution:
    def trap(self, height: List[int]) -> int:
        totalAmount = 0
        if not height or len(height) == 0:
            return totalAmount
        
        leftHighest = [0] * (len(height) + 1)
        leftHighest[0] = 0
        
        for i in range(len(height)):
            leftHighest[i + 1] = max(leftHighest[i], height[i])
        
        rightHighest = 0
        
        for i in range(len(height) - 1, -1, -1):
            rightHighest = max(height[i], rightHighest)
            if min(leftHighest[i], rightHighest) > height[i]:
                totalAmount += min(leftHighest[i], rightHighest) - height[i]
                
        return totalAmount