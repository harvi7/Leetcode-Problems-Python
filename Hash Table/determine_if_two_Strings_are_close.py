class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): 
            return False
        d1, d2 = collections.Counter(word1), collections.Counter(word2)
        return sorted(d1.values()) == sorted(d2.values()) and set(d1.keys()) == set(d2.keys())