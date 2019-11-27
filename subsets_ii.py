class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if not nums: return res 
        self.helper(nums, [], res)
        return res
        
    def helper(self, nums, pres, res):
        res.append(pres)    
        for idx, val in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            self.helper(nums[idx + 1:], pres + [val], res)
        