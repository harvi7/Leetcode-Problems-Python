class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        min_num = nums[0]
        for n in nums:
            min_num = min(min_num, n)
        res = 0
        for n in nums:
            res += n - min_num
        return res