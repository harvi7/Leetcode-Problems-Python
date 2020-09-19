class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        N = len(A)
        if N != len(B): return False
        if N == 0: return True     
        text, pattern = A + A, B 
        
        lps = self.computeTemporaryArray(pattern)
        i, j = 0, 0
        while i < len(text) and j < len(pattern):
            if text[i] == pattern[j]:
                i, j = i + 1, j + 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        if j == len(pattern):
            return True
        return False
    
    def computeTemporaryArray(self, pattern):
        lps = [0] * len(pattern)
        index, i = 0, 1
        while i < len(pattern):
            if pattern[i] == pattern[index]:
                lps[i] = index + 1
                index += 1
                i += 1
            else:
                if index != 0:
                    index = lps[index - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps