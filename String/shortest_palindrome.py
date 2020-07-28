# https://leetcode.com/problems/shortest-palindrome/discuss/441984/python-kmp-with-explanation

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        lps = self.getLPS(s + "#" + s[::-1])

        return s[lps[-1]:][::-1] + s

    def getLPS(self, s):
        lps = [0] * len(s)
        i, j = 0, 1

        while j < len(s): 
            if s[i] == s[j]: 
                lps[j] = i + 1
                i, j = i + 1, j + 1
            elif i != 0:
                i = lps[i - 1]
            else:
                lps[j] = 0
                j += 1
        return lps