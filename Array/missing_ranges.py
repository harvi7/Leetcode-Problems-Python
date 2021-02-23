class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            cur = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= cur - 1:
                result.append(self.formatRange(prev + 1, cur - 1))
            prev = cur
        return result
    
    def formatRange(self, lower, upper):
        if lower == upper: return f"{lower}"
        return f"{lower}->{upper}"