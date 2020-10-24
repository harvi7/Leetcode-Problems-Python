class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax, currMax = 0, 0      
        for i in nums: 
            prevMax, currMax = currMax, max(prevMax + i, currMax)            
        return currMax