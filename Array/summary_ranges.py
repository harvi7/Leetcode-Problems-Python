class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        length = len(nums)
        result = []
        i = 0
        while i < length:
            num = nums[i]
            while i + 1 < length and nums[i] + 1 == nums[i + 1]:
                i += 1
            if num != nums[i]:
                result.append(str(num) + "->" + str(nums[i]))
            else:
                result.append(str(num) + "")
            i += 1
        return result