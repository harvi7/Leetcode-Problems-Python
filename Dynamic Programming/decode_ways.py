class Solution:
    def numDecodings(self, s: str) -> int:
        def numDecodings(s, decodePointer, dp):
            def isValid(s):
                if len(s) == 0 or s[0] == '0':
                    return False
                value = int(s)
                return value >= 1 and value <= 26;
            
            if decodePointer >= len(s):
                return 1
            if dp[decodePointer] > -1:
                return dp[decodePointer]

            totalDecompositions = 0
            for i in range(1, 3):
                if decodePointer + i <= len(s):
                    snippet = s[decodePointer :decodePointer + i]
                    if isValid(snippet):
                        totalDecompositions += numDecodings(s, decodePointer + i, dp)

            dp[decodePointer] = totalDecompositions

            return dp[decodePointer]
        
        dp = [-1] * len(s)
        return numDecodings(s, 0, dp)