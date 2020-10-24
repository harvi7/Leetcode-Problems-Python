class Solution:
    def canWin(self, s: str) -> bool:
        self.winMap = {}
        return self.helper(s)
    
    def helper(self,s):
        if s in self.winMap:
            return self.winMap[s]
        
        for i in range(len(s) - 1):
            if s[i] =='+' and s[i + 1] == '+' and not self.helper(s[:i] + '--' + s[i + 2:]):
                self.winMap[s] = True
                return True
        self.winMap[s] = False
        return False