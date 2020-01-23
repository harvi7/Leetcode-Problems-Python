class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastGoodIndexPosition = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastGoodIndexPosition:
                lastGoodIndexPosition = i
        return lastGoodIndexPosition == 0