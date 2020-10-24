class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        return int(sum(int(n) for n in str(min(A))) % 2 == 0)