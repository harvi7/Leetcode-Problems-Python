class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        if len(nums) < 7:
            return False
        prefix = [0] * len(nums)
        prefix[0] = nums[0];
        for i in range(len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
        
        for j in range(3, len(nums) - 3):
            possible_targets = set()
            for i in range(1, j - 1):
                if prefix[i - 1] == prefix[j - 1] - prefix[i]:
                    possible_targets.add(prefix[i - 1])
            
            for k in range(j + 2, len(nums) - 1):
                if prefix[len(nums) - 1] - prefix[k] == prefix[k - 1] - prefix[j] and (prefix[k - 1] - prefix[j]) in possible_targets:
                    return True

        return False