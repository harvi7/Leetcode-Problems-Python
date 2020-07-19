# https://leetcode.com/problems/minimum-cost-for-tickets/discuss/560199/Python-DP-solutions-(recursive-%2B-iterative)

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]
        dp = [None]*(n+1)
        dp[0] = 0
    
        j = 0
        for i in range(1,n+1):
            if i == days[j]:
                dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
                j += 1
            else:
                dp[i] = dp[i-1]
        return dp[-1]