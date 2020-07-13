class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res , word_set = [], {w for w in words if w}
        
        for s in sorted(word_set, key=len, reverse=True):
            word_set.discard(s)
            
            if self.canBreak(s, word_set):
                res.append(s)
        
        return res
    
    def canBreak(self, s, word_set):
        if not word_set:
            return False
        n = len(s)
        if n == 0:
            return false
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(0, i):
                if not dp[j]:
                    continue
                if s[j : i] in word_set:
                    dp[i] = True
                    break    
        return dp[n]