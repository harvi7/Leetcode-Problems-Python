class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x > 0 or y > 0:
            res += (x % 2) ^ (y % 2)
            x >>= 1
            y >>= 1
        return res