class Solution:
    def countBits(self, num: int) -> List[int]:
        bitCounts = [0] * (num + 1)
        for i in range(1, num + 1):
            bitCounts[i] = bitCounts[i >> 1] + i % 2;
        return bitCounts