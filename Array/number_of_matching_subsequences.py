class Node:
     def __init__(self, w = "", i = 0):
        self.word = w
        self.index = i

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        ans = 0;
        heads = defaultdict(list)
        for word in words:
            heads[ord(word[0]) - ord('a')].append(Node(word, 0))

        for c in S:
            old_bucket = heads[ord(c) - ord('a')]
            heads[ord(c) - ord('a')] = []

            for node in old_bucket:
                node.index += 1
                if node.index == len(node.word):
                    ans += 1
                else:
                    heads[ord(node.word[node.index]) - ord('a')].append(node)
        return ans