class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        length = len(nums)
        if not nums or length == 0:
            return 0

        dp = [[0 for _ in range(length)] for _ in range(length)]

        for l in range(1, length + 1):
            for i in range(length - l + 1):
                j = i + l - 1
                for k in range(i, j + 1):
                    leftValue = 1
                    rightValue = 1
                    if i != 0:
                        leftValue = nums[i - 1]
                    if j != length -1:
                        rightValue = nums[j + 1]
                    
                    before = 0
                    after = 0
                    if i != k:
                        before = dp[i][k - 1]
                    if j != k:
                        after = dp[k + 1][j]

                    dp[i][j] = max(leftValue * nums[k] * rightValue + before + after, dp[i][j])
                        
        return dp[0][length - 1]