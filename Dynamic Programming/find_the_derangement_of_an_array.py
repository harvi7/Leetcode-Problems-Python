class Solution:
    def findDerangement(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 0
        first, second = 1, 0
        for i in range(2, n + 1):
            temp = second
            second = int(((i - 1) * (first + second)) % 1000000007)
            first = temp
        return second;