class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0: return -1
        prevRemainder = 0
        for length_N in range(1,K+1):
            prevRemainder = (prevRemainder * 10 + 1) % K
            if prevRemainder == 0:
                return length_N
        return -1