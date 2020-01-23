class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        
        i, j = 0, len(nums) - 1
        
        while i + 1 <= len(nums) - 1 and nums[i] <= nums[i + 1]: 
            i += 1
        while j - 1 >= 0 and nums[j-1] <= nums[j]: 
            j -= 1
       
        m, M = float('inf'), -float('inf')
        for n in nums[i : j + 1]:
            m = min(m, n)
            M = max(M, n)
        
        while i - 1 >= 0 and nums[i - 1] > m: 
            i -= 1
        while j + 1 <= len(nums) - 1 and nums[j + 1] < M: 
            j += 1
        
        ans = j - i + 1
        return ans if ans >= 0 else 0