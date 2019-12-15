class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        if len(s) < 10: return res
        seen, repeated, i = set(), set(), 0        
        while i + 10 <= len(s):
            subseq = s[i : i + 10]
            i += 1
            if subseq not in seen:
                seen.add(subseq)
            else:
                repeated.add(subseq)
        return repeated