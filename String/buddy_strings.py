class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        mapA, pos = {}, []
        for i in range(len(A)):      
            if A[i] != B[i]:
                pos.append(i)
            if len(pos) > 2:
                return False
            
            mapA[A[i]] = mapA.get(A[i], 0) + 1
            
        if A == B:
            for c in mapA.keys():
                if mapA[c] > 1:
                    return True
            return False
        
        if len(pos) != 2:
            return False
        posOne = pos[0]
        posTwo = pos[1]
        return A[posOne] == B[posTwo] and A[posTwo] == B[posOne]