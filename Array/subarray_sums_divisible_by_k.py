class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        counts = [0] * K
        sumCurr = 0
        for x in A:
            sumCurr += (x % K + K) % K
            counts[sumCurr % K] += 1

        result = counts[0]
        for c in counts:
            result += (c * (c - 1)) // 2
        return result