class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        ans = ''
        for c in word:
            if c not in node.children: break
            node = node.children[c]
            ans += c
            if node.isWord: return ans
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for letter in dictionary:
            trie.insert(letter)
        res = ''
        for word in sentence.split():
            if res:
                res += ' '
            res += trie.search(word)
        return res
        