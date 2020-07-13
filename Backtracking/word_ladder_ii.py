# https://leetcode.com/problems/word-ladder-ii/discuss/269012/Python-BFS%2BBacktrack-Greatly-Improved-by-bi-directional-BFS

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList:
            return []
        found, startSet, endSet, nq, rev = False, {beginWord}, {endWord}, set(), False
        while startSet and not found:
            words -= set(startSet)
            for x in startSet:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y in endSet: 
                            found = True
                        else: 
                            nq.add(y)
                        tree[y].add(x) if rev else tree[x].add(y)
            startSet, nq = nq, set()
            if len(startSet) > len(endSet): 
                startSet, endSet, rev = endSet, startSet, not rev
        def bt(x): 
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        return bt(beginWord)