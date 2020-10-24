class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] == -1: continue 
            count = 0
            while nums[i] != -1: # 
                nums[i], i = -1, nums[i]
                count += 1
            if count > res: res = count
        return res