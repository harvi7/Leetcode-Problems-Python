class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        
        dp = [1] * (n + 1)
        nums.sort();
        max_num = 1
        
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    if max_num < dp[i]:
                        max_num = dp[i]
                
        subset, prev = [], -1
        for i in range(n - 1, -1, -1):
            if dp[i] == max_num and (prev % nums[i] == 0 or prev == -1):
                subset.append(nums[i])
                max_num -= 1
                prev = nums[i]       
        return subset