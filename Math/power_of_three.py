class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        res = round(log(n, 3))
        return 3**res == n