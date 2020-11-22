class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
       
        if not nums or len(nums) == 0:
            return res
        used = [False] * len(nums)
        self.helper(nums, [], used, res)
        return res
    
    def helper(self, nums, permutation, used, res):
        if len(permutation) == len(nums):
            res.append(permutation[:])
            return

        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True
            permutation.append(nums[i])
            self.helper(nums, permutation, used, res)
            permutation.pop()
            used[i] = False
    
    