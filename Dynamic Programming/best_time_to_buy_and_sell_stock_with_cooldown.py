class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         length = len(prices)
#         if length <= 1:
#             return 0
#         if length == 2 and prices[1] > prices[0]:
#             return prices[1] - prices[0]
#         elif length == 2 and prices[0] > prices[1]:
#             return 0
        
#         dp = [[0 for _ in range(2)] for _ in range(length)]
        
#         dp[0][0] = 0
#         dp[0][1] = -prices[0]
#         dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
#         dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
        
#         for i in range(2, length):
#             dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
#             dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
#         return dp[length - 1][0]
        sold, held, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)

        return max(sold, reset)