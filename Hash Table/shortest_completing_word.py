class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def count(word):
            result = [0] * 26
            for letter in word:
                result[ord(letter) - ord('a')] += 1
            return result

        def dominates(c1, c2):
            return all(x2 <= x1 for x1, x2 in zip(c1, c2))

        ans = ""
        target = count(c.lower() for c in licensePlate if c.isalpha())
        for word in words:
            if (not ans or (len(word) < len(ans))) and dominates(count(word.lower()), target):
                ans = word

        return ans