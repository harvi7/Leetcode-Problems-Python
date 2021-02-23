class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)
        for s in sorted(strs, key = len, reverse = True):
            if sum(isSubsequence(s, t) for t in strs) == 1:
                return len(s)
        return -1