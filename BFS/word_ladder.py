class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        if endWord not in s:
            return 0
        q = deque()
        q.append((beginWord, 1))
        v = set()
        while q:
            word, dep = q.popleft()
            if word == endWord:
                return dep
            # w * 26 => w
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    w = word[0:i] + c + word[i + 1:len(word)]
                    if w in s and w not in v:
                        v.add(w)
                        q.append((w, dep + 1))
        
        return 0