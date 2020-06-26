class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        for i in range(len(points) - 1):
            first = points[i]
            second = points[i + 1]
            
            xDiff = abs(first[0] - second[0])
            yDiff = abs(first[1] - second[1])
            
            seconds += max(xDiff, yDiff)
        return seconds