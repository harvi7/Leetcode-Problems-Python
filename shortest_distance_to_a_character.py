class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n, res = len(S), [] 
        cPosition = -n        
        
        for i in range(n):
            if S[i] == C:
                cPosition = i
            res.append(i - cPosition)
        
        for i in range(n - 1, -1, -1):
            if S[i] == C:
                cPosition = i
            res[i] = min(res[i], abs(i - cPosition))
        return res