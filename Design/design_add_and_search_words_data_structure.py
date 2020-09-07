class TrieNode:
    
    def __init__(self):
        self.trie = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        
        self.buildTree(word)
        
    def buildTree(self, word):
        cur = self.root
        
        for char in word:
            cur = cur.trie[char]
        
        cur.isWord = True
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        return self.find(word, 0, self.root)
    
    def find(self, word, index, node):
        
        if node is None:
            return False
        
        elif index == len(word):
            return node.isWord
        
        if word[index] == '.':
            for child_node in node.trie.values():
                if self.find(word, index + 1, child_node):
                    return True    
            return False
        else:
            return node and self.find(word, index + 1, node.trie.get(word[index]))
        