class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxi, ans = values[0] + 0, 1
        n = len(values)
        for i in range(1, n):
            ans = max(ans, maxi + values[i] - i)
            maxi = max(maxi, values[i] + i)
        return ans