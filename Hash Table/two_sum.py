class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement not in dic:
                dic[num] = i
            else:
                return [dic[complement], i]