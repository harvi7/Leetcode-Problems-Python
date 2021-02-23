class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = list(p)
        s = list(s)
        writeIndex = 0
        isFirst = True
        for i in range(len(p)):
            if p[i] == '*':
                if isFirst:
                    p[writeIndex] = p[i]
                    writeIndex += 1
                    isFirst = False
            else:
                p[writeIndex] = p[i]
                writeIndex += 1
                isFirst = True

        T = [[False] * (writeIndex + 1) for _ in range(len(s) + 1)]
        
        if writeIndex > 0 and p[0] == '*':
            T[0][1] = True

        T[0][0] = True

        for i in range(1, len(T)):
            for j in range(1, len(T[0])):
                if p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    T[i][j] = T[i - 1][j - 1];
                elif p[j - 1] == '*':
                    T[i][j] = T[i - 1][j] or T[i][j - 1]

        return T[len(s)][writeIndex]