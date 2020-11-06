class Solution:
    def minInsertions(self, s: str) -> int:
        res, right = 0, 0
        for i in range (len(s)):
            if s[i] == '(':
                if right % 2 > 0:
                    right -= 1
                    res += 1
                right += 2
            else:
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
                    
        return right + res