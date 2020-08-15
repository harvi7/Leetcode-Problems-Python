class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max, current_min, final_max = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            temp = current_max
            current_max = max(nums[i], nums[i]*current_max, nums[i]*current_min)
            current_min = min(nums[i], nums[i]*temp, nums[i]*current_min)
            final_max = max(final_max, current_max)
        return final_max