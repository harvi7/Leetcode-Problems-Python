# https://leetcode.com/problems/relative-ranks/discuss/822719/Python-or-simple-solution-using-reverse-sort

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        temp = sorted(nums,reverse=True)
    
        for i,n in enumerate(nums): 

            rank = temp.index(n)

            if rank == 0: 
                nums[i] = "Gold Medal"
            elif rank == 1:
                nums[i] = "Silver Medal"
            elif rank == 2:
                nums[i] = "Bronze Medal"
            else: 
                nums[i] = str(rank + 1)

        return nums