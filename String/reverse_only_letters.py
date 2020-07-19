class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        string = list(S)
        
        start = 0
        end = len(S) - 1
        
        while start <= end:
            while start < end and not string[start].isalpha():
                start += 1
            while end > start and not string[end].isalpha():
                end -= 1
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1
        
        return ''.join(string)