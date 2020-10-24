class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        res = sums
        for i in range(k, len(nums)):
            sums += nums[i] - nums[i - k]
            if res < sums:
                res = sums
        return res / k