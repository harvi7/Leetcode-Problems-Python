class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s is None or t is None or len(s) != len(t): return False
        map = {}
        for i in range(0, len(s)):
            if s[i] in map:
                if map.get(s[i]) == t[i]: continue
                else: return False
            else:
                if t[i] not in map.values(): map[s[i]] = t[i]
                else: return False
        return True