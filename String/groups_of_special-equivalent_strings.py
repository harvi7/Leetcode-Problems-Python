class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res = set()
        for s in A:
            s = ''.join(sorted(s[::2]) + sorted(s[1::2]))
            res.add(s)
        return len(res)