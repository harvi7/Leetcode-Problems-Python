class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i in range(0, len(nums)):
            if nums[i] in map and i - map.get(nums[i]) <= k:
                return True
            else:
                map[nums[i]] = i
        return False