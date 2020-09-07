class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        new_s, new_t = [], []
        
        for i in S:
            if i == '#':
                if new_s:
                    new_s.pop()
            else:
                new_s.append(i)
                
        for j in T:
            if j == '#':
                if new_t:
                    new_t.pop()
            else:
                new_t.append(j)
        
        return new_s == new_t