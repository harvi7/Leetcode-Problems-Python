class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        char_counts = [0] * 26
        
        for i in range(len(s)):
            char_counts[ord(s[i]) - 97] += 1
            char_counts[ord(t[i]) - 97] -= 1
        
        for count in char_counts:
            if count != 0: return False
        
        return True 