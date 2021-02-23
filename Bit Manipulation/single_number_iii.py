class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num

        diff = bitmask & (-bitmask)       
        x = 0
        for num in nums:
            if num & diff:
                x ^= num
       
        return [x, bitmask^x]