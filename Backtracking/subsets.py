# https://leetcode.com/problems/subsets/discuss/363804/Python-4-ms-beats-100.00-The-shortest-solution-ever-%2B-image-explanation

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def inner(nums, subset, res):
            for i, num in enumerate(nums):
                inner(nums[i + 1:], subset + [num], res)
            res.append(subset)
        inner(nums, [], res)
        return res