class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.dp[i + 1] = self.dp[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j + 1] - self.dp[i];
