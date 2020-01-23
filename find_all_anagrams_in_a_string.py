# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/394531/Easy-to-understand-O(n)-python-solution

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ref = [0] * 26
        curr = [0] * 26
        for c in p:
            ref[ord(c) - ord('a')] += 1
        idx = 0
        result = []
        while idx < len(s):
            curr[ord(s[idx]) - ord('a')] += 1
            if ref == curr:
                result.append(idx + 1 - len(p))
            if idx + 1 - len(p) >= 0:
                curr[ord(s[idx + 1 - len(p)]) - ord('a')] -= 1
            idx += 1
        return result
    