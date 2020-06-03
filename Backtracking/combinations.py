# https://leetcode.com/problems/combinations/discuss/417953/Python3-Easy-to-understand-Backtracking

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        
        if n == k:
            return [list(range(1, n + 1))]
        
        result = []
        self.helper(result, [], 1, n, k)
        return result
    
    def helper(self, result, currentList, start, n, k): 
        if k == 0:
            result.append(currentList)
            return
        for i in range(start, n + 1):
            self.helper(result, currentList + [i], i + 1, n, k - 1)