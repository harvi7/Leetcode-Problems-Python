class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(nums, target, first):
            left, right, result = 0, len(nums) - 1, -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    result = mid
                    if first: right = mid - 1
                    else: left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1 
            return result
        
        res = [-1, -1]
        if not nums or len(nums) == 0: return res
        first = find(nums, target, True)
        if first == -1: return res
        last = find(nums, target, False)
        res[0], res[1] = first, last
        return res
