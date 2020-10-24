class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N  
        res[0] = 1
        for i in range(1, N):
            res[i] = nums[i - 1] * res[i - 1]
        R = 1
        for i in range(N - 1, -1, -1):
            res[i] = res[i] * R
            R = R * nums[i]
        return res