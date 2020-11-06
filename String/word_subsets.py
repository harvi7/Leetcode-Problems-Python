# https://leetcode.com/problems/word-subsets/discuss/659164/Python-90-with-comments-and-explanation 

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
#         def count(word):
#             ans = [0] * 26
#             for letter in word:
#                 ans[ord(letter) - ord('a')] += 1
#             return ans

#         bmax = [0] * 26
#         for b in B:
#             for i, c in enumerate(count(b)):
#                 bmax[i] = max(bmax[i], c)

#         ans = []
#         for a in A:
#             if all(x >= y for x, y in zip(count(a), bmax)):
#                 ans.append(a)
#         return ans
        subset = {}
        
        for b in B:
            for char in b: 
                subset[char] = max(b.count(char), subset.get(char, 0))
        ans = []
        for a in A:
            if all(a.count(char) >= subset[char] for char in subset.keys()):
                ans.append(a)
                
        return ans