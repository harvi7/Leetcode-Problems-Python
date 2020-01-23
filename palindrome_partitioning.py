class Solution:
    def partition(self, s: str) -> List[List[str]]:
        decompositions = []
        self.decomposeString(s, [], decompositions)
        return decompositions
    
    def decomposeString(self, s, partialDecomposition, decompositions):
        if not s:
            decompositions.append(partialDecomposition)
            return
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.decomposeString(s[i:], partialDecomposition+[s[:i]], decompositions)

    def isPalindrome(self, s):
        return s == s[::-1]
                