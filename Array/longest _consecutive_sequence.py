class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        while nums:
            x = nums.pop()
            lower_bound = x - 1
            while lower_bound in nums:
                nums.remove(lower_bound)
                lower_bound -= 1
            
            upper_bound = x + 1
            while upper_bound in nums:
                nums.remove(upper_bound)
                upper_bound += 1
            res = max(res, upper_bound - lower_bound - 1)
        return res