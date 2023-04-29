class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while (left < right):
                sum = nums[i] + nums[left] + nums[right]
                if abs(target - sum) < abs(target - closest):
                    closest = sum
                if sum < target:
                    left += 1
                else:
                    right -= 1
            if sum == target:
                return sum
        return closest