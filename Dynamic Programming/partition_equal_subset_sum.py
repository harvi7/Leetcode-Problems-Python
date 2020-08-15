class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[target] = True
        for i in range(len(nums)):
            if nums[i] > target: return False
            if dp[nums[i]]: return True
            for j in range(1, target + 1):
                if dp[j] and j - nums[i] > 0:
                    dp[j - nums[i]] = True
        return False