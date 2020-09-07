class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words or len(words) < 2:
            return True
        charMap = {char:index for index, char in enumerate(order)}
        word_index = [[charMap[char] for char in w] for w in words]
        
        return all(w1 <= w2 for w1, w2 in zip(word_index, word_index[1:]))