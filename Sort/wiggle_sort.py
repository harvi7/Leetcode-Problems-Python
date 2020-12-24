class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            nums[i : i + 2] = sorted(nums[i : i + 2], reverse = i % 2)