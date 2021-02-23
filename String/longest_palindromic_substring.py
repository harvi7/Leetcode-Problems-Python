class Solution:
    def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         # Form a bottom-up dp 2d array
#         # dp[i][j] will be 'true' if the string from index i to j is a palindrome. 
#         dp = [[False] * n  for _ in range(n)]
        
#         ans = ''
#         # every string with one character is a palindrome
#         for i in range(n):
#             dp[i][i] = True
#             ans = s[i]
            
#         maxLen = 1
#         for start in range(n - 1, -1, -1):
#             for end in range(start + 1, n):             
# 				# palindrome condition
#                 if s[start] == s[end]:
#                     # if it's a two char. string or if the remaining string is a palindrome too
#                     if end - start == 1 or dp[start + 1][end - 1]:
#                         dp[start][end] = True
#                         if maxLen < end - start + 1:
#                             maxLen = end - start + 1
#                             ans = s[start: end+ 1]
        
#         return ans
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start : end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1