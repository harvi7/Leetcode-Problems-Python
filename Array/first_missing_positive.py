class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        contains_one = False
        for x in nums:
            if x == 1:
                contains_one = True
                break
        
        if not contains_one: return 1
        
        n = len(nums)
        if n == 1: return 2
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n: nums[i] = 1
        
        for i in range(n):
            x = abs(nums[i])
            if nums[x - 1] > 0: nums[x - 1] *= -1
        
        for i in range(n):
            if nums[i] > 0: return i + 1
        
        return n + 1