class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1map = [0] * 26
        s2map = [0] * 26
        i = 0
        while i < len(s1):
            s1map[ord(s1[i]) - ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] += 1
            i += 1
        
        if s1map == s2map: return True
        
        left = 0; right = i
        while right < len(s2):
            s2map[ord(s2[right]) - ord('a')] += 1
            s2map[ord(s2[left]) - ord('a')] -= 1
            left += 1; right += 1
            
            if s1map == s2map: return True
        
        return False