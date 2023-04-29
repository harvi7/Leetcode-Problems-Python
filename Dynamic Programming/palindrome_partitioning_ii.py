class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        isPal = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        self.computeAllPals(isPal, s)
        
        minPals = [float('inf')] * (n + 2)
        minPals[n + 1] = 0
        
        for k in range(n, 0, -1):
            for l in range(k, n + 1):
                if isPal[k][l]:
                    minPals[k] = min(minPals[k], 1 + minPals[l + 1])
        
        return minPals[1] - 1
    
    def computeAllPals(self,isPal, A):
        n = len(A)
        for i in range(n, 0, -1):
            isPal[i][i - 1] = True
            isPal[i][i] = True
            
            for j in range(i + 1, n + 1):
                if A[i - 1] == A[j - 1]:
                    isPal[i][j] = isPal[i + 1][j - 1]
                else:
                    isPal[i][j] = False