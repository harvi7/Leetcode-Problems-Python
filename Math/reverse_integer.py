class Solution:
    def reverse(self, x: int) -> int:
        res, remains = 0, abs(x)

        while remains:
            res, remains = res * 10 + remains % 10, remains // 10    

        if x < 0: res *= -1

        return res if abs(res) < 0x7fffffff else 0