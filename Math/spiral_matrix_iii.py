class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        directions = [0, 1, 0, -1, 0]
        result = [[0, 0] for _ in range(R * C)]
        i = 0
        result[i] = [r0, c0]
        i += 1
        length = 0
        d = 0
        while i < R * C:
            if d == 0 or d == 2:
                length += 1
            for k in range(length):
                r0 += directions[d]
                c0 += directions[d + 1]
                if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                    result[i] = [r0, c0]
                    i += 1
            d = (d + 1) % 4
        return result