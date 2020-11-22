class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, i = 0, 0
        index = {}
        for j, c in enumerate(s):
            if c in index and i <= index[c]:
                i = index[c] + 1
            ans = max(ans, j - i + 1)
            index[c] = j
        return ans