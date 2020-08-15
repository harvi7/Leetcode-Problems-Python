import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        maxHeap = []
        for (x, y) in points:
            dist = -(x * x + y * y)
            if len(maxHeap) == K:
                heapq.heappushpop(maxHeap, (dist, x, y))
            else:
                heapq.heappush(maxHeap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in maxHeap]