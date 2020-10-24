class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        index1 = index2 = float('inf')
        result = float('inf')

        for i, w in enumerate(words):
            if w == word1: index1 = i
            elif w == word2: index2 = i
            result = min(abs(index2 - index1), result)
        return result