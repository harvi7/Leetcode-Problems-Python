class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def backtrack(index, remain, comb):
            if remain == 0 and len(comb) == k:
                results.append(comb)
                return
            
            for i in range(index, 10):
                if remain < i: break
                backtrack(i + 1, remain - i, comb + [i])
                comb.pop
                
        
        
        backtrack(1, n, [])
        return results