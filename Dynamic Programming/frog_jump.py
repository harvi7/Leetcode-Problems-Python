# https://leetcode.com/problems/frog-jump/discuss/88800/Python-Documented-solution-that-is-easy-to-understand

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        d = {x: set() for x in stones}
        d[1].add(1)
        for x in stones[:-1]:            
            for j in d[x]: 
                for k in range(j - 1, j + 2):
                    if k > 0 and x + k in d:
                        d[x + k].add(k)
        return bool(d[stones[-1]])
    