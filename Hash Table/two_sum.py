class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        num_idx_dict = dict()
        
        for i in range(len(nums)):
            if target - nums[i] in num_idx_dict:
                result[1] = i
                result[0] = num_idx_dict.get(target - nums[i])
            num_idx_dict[nums[i]] = i
        return result