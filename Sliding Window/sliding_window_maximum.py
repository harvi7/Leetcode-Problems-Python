class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) == 0 or k > len(nums):
            return [0]
        
        res, dq = [], []
        i = 0
        
        while i < len(nums):
            if dq and dq[0] == i - k:
                dq.pop(0)
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            if i >= k - 1:
                res.append(nums[dq[0]])
            i += 1
        return res