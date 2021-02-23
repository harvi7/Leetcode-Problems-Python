class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seenOnce, seenTwice = 0, 0

        for num in nums:
            seenOnce = ~seenTwice & (seenOnce ^ num)
            seenTwice = ~seenOnce & (seenTwice ^ num)
        return seenOnce