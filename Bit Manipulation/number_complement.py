class Solution:
    def findComplement(self, num: int) -> int:
        result, i = 0, 0
        while num:
            if (num & 1) == 0:
                result += 1 << i
            i += 1
            num >>= 1
        return result