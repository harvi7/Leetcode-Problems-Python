# https://leetcode.com/problems/word-search-ii/discuss/719552/easy-to-understand-python-code-with-Trie-and-dfs

class TrieNode():
    def __init__(self):
        self.children = [None]*26 # for 26 letters of from 'a' to 'z'
        self.word = None # record the word str

class Trie():
    def __init__(self, words):
        self.root = TrieNode()
        self.insertGroup(words)
        
    def insert(self, word):
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.word = word
    
    def insertGroup(self, words):
        for word in words:
            self.insert(word)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(words)
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfsTrie2(board, trie.root, i, j, res)
        return res
    
    def dfsTrie2(self, board, node, i, j, res):
        char = board[i][j]
        
        if char == '#' or not node.children[ord(char) - ord('a')]:
            return
        node = node.children[ord(char) - ord('a')]
        if node.word:
            res.append(node.word)
            node.word = None # de-duplicate
        board[i][j] = '#' # mark that current position in board is already visited
        if i > 0:
            self.dfsTrie2(board, node, i-1, j, res)
        if i < len(board)-1:
            self.dfsTrie2(board, node, i+1, j, res)
        if j > 0:
            self.dfsTrie2(board, node, i, j-1, res)
        if j < len(board[0])-1:
            self.dfsTrie2(board, node, i, j+1, res)
            
        board[i][j] = char # after dfs, recover current position [i][j]'s original char value
        

