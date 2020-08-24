class Solution:
    def reverseWords(self, s: str) -> str:
        result, word = "", ""
        for i in range(len(s)):
            if s[i] != ' ':
                word += s[i]
            else:
                result += word[::-1] + " "
                word = ""
        result += word[::-1]
        return result