class Solution:
    def maximumSwap(self, num: int) -> int:    
        numChars = [int(i) for i in str(num)]
        for i in range(len(numChars)-1):
            m = max(numChars[i + 1 :])
            if numChars[i] < m:
                for j in range(len(numChars) - 1, i, -1):
                    if numChars[j] == m:
                        numChars[i], numChars[j] = numChars[j], numChars[i]
                        return int("".join([str(i) for i in numChars]))
        return num