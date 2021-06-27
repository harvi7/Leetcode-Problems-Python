class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        D = {x: i for i, x in enumerate(nums2)}
        return [D[x] for x in nums1]