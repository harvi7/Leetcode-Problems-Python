class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        firstNegative, zeroPosition, count, res = -1, -1, 0, 0;
        for i in range (len(nums)):
            if nums[i] < 0:
                count += 1
                if firstNegative == -1: firstNegative = i

            if nums[i] == 0:
                count = 0
                firstNegative = -1
                zeroPosition = i
            else:
                if count % 2 == 0: res = max(i - zeroPosition, res)
                else: res = max(i - firstNegative, res)
        return res