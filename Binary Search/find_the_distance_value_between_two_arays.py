class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        arr2.sort()
        l = len(arr2)
        for num in arr1:
            index = bisect.bisect_left(arr2, num)
            min_dist = float('inf')
            if index > 0:
                min_dist = min(min_dist, abs(num - arr2[index - 1]))
            if index < l:
                min_dist = min(min_dist, abs(num - arr2[index]))
            if min_dist > d:
                count += 1
        return count