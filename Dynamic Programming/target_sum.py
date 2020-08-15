class Solution:
    def findTargetSumWays(self, A, S):
        def subsetSum(nums, s):
            dp = [0] * (s + 1) 
            dp[0] = 1
            for num in nums:
                for i in range(s, num - 1, -1):
                    dp[i] += dp[i - num] 
            return dp[s]
            
        sumTot = sum(A)
        return 0 if sumTot < S or (S + sumTot) % 2 > 0 else subsetSum(A, (S + sumTot) // 2) 