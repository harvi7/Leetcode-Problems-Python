class Solution:
    def numDecodings(self, s: str) -> int:
#         def numDecodings(s, decodePointer, dp):
#             def isValid(s):
#                 if len(s) == 0 or s[0] == '0':
#                     return False
#                 value = int(s)
#                 return value >= 1 and value <= 26;
            
#             if decodePointer >= len(s):
#                 return 1
#             if dp[decodePointer] > -1:
#                 return dp[decodePointer]

#             totalDecompositions = 0
#             for i in range(1, 3):
#                 if decodePointer + i <= len(s):
#                     snippet = s[decodePointer :decodePointer + i]
#                     if isValid(snippet):
#                         totalDecompositions += numDecodings(s, decodePointer + i, dp)

#             dp[decodePointer] = totalDecompositions

#             return dp[decodePointer]
        
#         dp = [-1] * len(s)
#         return numDecodings(s, 0, dp)
        if s == "": return 0
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i-1] != "0":
                dp[i] += dp[i - 1]
            if i != 1 and s[i - 2 : i] < "27" and s[i-2:i] > "09": 
                dp[i] += dp[i - 2]
        return dp[len(s)]