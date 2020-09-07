# https://leetcode.com/problems/increasing-subsequences/discuss/804364/Python-backtrack-with-Set

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = set()
        leng = len(nums)
        
        def backtrack(currArray, start):
            if len(currArray) > 1:
                t = tuple(currArray)
                if t not in result:
                    result.add(t)

            if start >= leng:
                return
            
            for i in range(start, leng):
                currLeng = len(currArray)
                if  currLeng >0 and nums[i] < currArray[currLeng-1]:
                    continue
                    
                currArray.append(nums[i])
                backtrack(currArray, i + 1)
                currArray.pop()
        
        backtrack([], 0)
        return result
    

        