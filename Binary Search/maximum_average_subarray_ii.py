class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        right, left = max(nums), min(nums)

        while right - left > 1e-5:
            mid = (right + left) / 2
            if self.check(nums, mid, k): left = mid
            else: right = mid
        return left
    
    def check(self, nums, mid, k):
        currSum, prevSum, minSum = 0, 0, 0
        for i in range(len(nums)):
            currSum += nums[i] - mid
            if i >= k - 1:
                if currSum - minSum >= 0: return True
                prevSum += nums[i - k + 1] - mid
                minSum = min(minSum, prevSum)
        return False