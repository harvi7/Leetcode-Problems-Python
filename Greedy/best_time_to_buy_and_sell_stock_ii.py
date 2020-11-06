class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1: return 0
        maxProfit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                maxProfit += prices[i + 1] - prices[i]
        return maxProfit