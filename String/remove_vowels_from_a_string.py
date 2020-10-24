class Solution:
    def removeVowels(self, S: str) -> str:
        return ''.join(e for e in S if e not in 'aeiou')