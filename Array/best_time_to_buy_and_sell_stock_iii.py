import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        firstBuy, firstSell = -math.inf, 0              
        secondBuy, secondSell = -math.inf, 0             
        for p in prices:
            firstBuy = max(firstBuy, -p)
            firstSell = max(firstSell, p + firstBuy)
            secondBuy = max(secondBuy, firstSell - p)     
            secondSell = max(secondSell, secondBuy + p)  
        return secondSell