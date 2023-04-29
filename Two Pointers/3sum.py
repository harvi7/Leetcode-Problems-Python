class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        if not nums or len(nums) < 3: return  
        nums.sort()

        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                low, high = i + 1, len(nums) - 1
                currSum = -nums[i]

                while low < high:
                    if nums[low] + nums[high] == currSum:
                        result.append([nums[i], nums[low], nums[high]])
                        
                        while low < high and nums[low] == nums[low + 1]: low += 1
                        while low < high and nums[high] == nums[high - 1]: high -= 1
                        
                        low += 1
                        high -= 1    

                    elif nums[low] + nums[high] > currSum:
                        high -= 1
                    else:
                        low += 1

        return result