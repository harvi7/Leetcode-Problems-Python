class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0;
        left = 2
        for right in range(2, len(nums)):
            if nums[left - 2] != nums[right]:
                nums[left] = nums[right]
                left += 1
        return left