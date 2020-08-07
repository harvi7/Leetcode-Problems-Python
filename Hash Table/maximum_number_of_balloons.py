class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        i, j, k, l, m = text.count('b'), text.count('a'), text.count('l')//2, text.count('o')//2, text.count('n')
        return min([i, j, k, l, m])