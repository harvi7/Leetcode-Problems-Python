class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        totalCost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            c = heapq.heappop(sticks) + heapq.heappop(sticks)
            totalCost += c
            heapq.heappush(sticks, c)
        return totalCost