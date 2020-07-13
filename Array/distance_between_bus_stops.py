class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwiseDist, totalDist = 0, 0
        for i in range(len(distance)):
            if start < destination and (i >= start and i < destination):
                clockwiseDist += distance[i]
            if start > destination and (i >= start or i < destination):
                clockwiseDist += distance[i]
            totalDist += distance[i]        
        return min(clockwiseDist, totalDist - clockwiseDist)