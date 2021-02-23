import collections

class Solution:
    def longestWord(self, words: List[str]) -> str:
#         wordset = set(words)
#         words.sort(key = lambda c: (-len(c), c))
#         for word in words:
#             if all(word[:k] in wordset for k in range(1, len(word))):
#                 return word

#         return ""
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans