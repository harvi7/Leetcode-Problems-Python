class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        start = 0
        end = len(s) - 1
        
        while start <= end:
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
            elif s[end] not in vowels:
                end -= 1
                continue
            elif s[start] not in vowels:
                start += 1
                continue
            start += 1
            end -= 1
        
        return ''.join(s)