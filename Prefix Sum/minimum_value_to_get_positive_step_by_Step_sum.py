class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minVal, total = 0, 0

        for num in nums:
            total += num;
            minVal = min(minVal, total)

        return -minVal + 1