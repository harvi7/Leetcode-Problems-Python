class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        list.sort(coins)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                else: break

        return -1 if dp[amount] > amount else dp[amount]