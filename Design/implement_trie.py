class TrieNode:
    isWord = False
    children = []
    def __init__(self, val):
        self.val = val
        self.children = [None] * 26
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in range(len(word)):
            c = word[i]
            if not node.children[ord(c) - ord('a')]:
                node.children[ord(c) - ord('a')] = TrieNode(c)
            node = node.children[ord(c) - ord('a')]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in range(len(word)):
            c = word[i]
            if not node.children[ord(c) - ord('a')]:
                return False
            node = node.children[ord(c) - ord('a')]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root 
        for i in range(len(prefix)):
            c = prefix[i]
            if not node.children[ord(c) - ord('a')]:
                return False
            node = node.children[ord(c) - ord('a')]
        return True