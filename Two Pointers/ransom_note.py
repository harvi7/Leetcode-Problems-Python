class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        for c in magazine:
            counts[c] = counts.get(c, 0) + 1
        
        for c in ransomNote:
            if c not in magazine or counts[c] <= 0: 
                return False
            counts[c] = counts.get(c) - 1
        
        return True