class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, val_sum, result = 0, 0, float('inf')
        for i in range(len(nums)):
            val_sum += nums[i]
            while val_sum >= s:
                result = min(result, i + 1 - left)
                val_sum -= nums[left]
                left += 1
        return 0 if result == float('inf') else result
    s