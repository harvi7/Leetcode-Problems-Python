class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        result, i = 0, 0
        while N:
            if (N & 1) == 0:
                result += 1 << i
            i += 1
            N >>= 1
        return result 