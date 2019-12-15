class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        i = length // 2
        while i >= 1:
            if length % i == 0:
                numRepeats = length // i
                substring = s[0:i]
                sb = ""
                for _ in range(numRepeats): 
                    sb += substring
                if sb == s:
                    return True
            i -= 1 
        return False