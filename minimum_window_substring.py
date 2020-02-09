class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or len(s) < len(t) or len(s) == 0 or len(t) == 0: return ""
        requiredCharacters = {}
        for c in t: 
            requiredCharacters[c] = requiredCharacters.get(c, 0) + 1

        left = 0
        minLeft = 0
        minLen = len(s) + 1
        count = 0
        
        for right in range(len(s)):
            if s[right] in requiredCharacters:
                requiredCharacters[s[right]] = requiredCharacters[s[right]] - 1
                if requiredCharacters[s[right]] >= 0: count += 1
                while count == len(t):
                    if right - left + 1 < minLen:
                        minLeft = left
                        minLen = right - left + 1

                    if s[left] in requiredCharacters:
                        requiredCharacters[s[left]] =  requiredCharacters[s[left]] + 1
                        if requiredCharacters[s[left]] > 0: count -= 1
                    left += 1 
        if minLen > len(s): return ""  
    
        return s[minLeft : minLeft + minLen]