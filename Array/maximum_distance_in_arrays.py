class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res, min_val, max_val = 0, arrays[0][0], arrays[0][len(arrays[0]) - 1];
        for i in range(1, len(arrays)):
            res = max(res, max(abs(arrays[i][len(arrays[i]) - 1] - min_val), abs(max_val - arrays[i][0])))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][len(arrays[i]) - 1])
        return res