class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindromesAroundCenter(lo, hi):
            ans = 0
            while lo >= 0 and hi < len(s):
                if s[lo] != s[hi]:
                    break 
                lo, hi, ans = lo - 1, hi + 1, ans + 1
            return ans
            
        res = 0
        for i in range(0, len(s)):
            res += countPalindromesAroundCenter(i, i)
            res += countPalindromesAroundCenter(i, i + 1)

        return res