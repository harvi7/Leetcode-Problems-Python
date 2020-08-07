class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_map, res = {}, 0
        for num in nums: 
            num_map[num] = num_map.get(num, 0) + 1
        for key in num_map.keys(): 
            if key + 1 in num_map:
                res = max(res, num_map[key] + num_map[key + 1])
        return res