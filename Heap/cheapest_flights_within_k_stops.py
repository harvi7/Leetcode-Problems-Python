class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        g = [[0] * n for _ in range(n)]
        for f in flights:
            g[f[0]][f[1]] = f[2]
        
        heap = []
        heapq.heappush(heap, (0, src, K + 1))
        
        while heap:
            cur = heapq.heappop(heap)
            price, place, remainStops = cur[0], cur[1], cur[2]     
            if place == dst:
                return price
            
            if remainStops > 0:
                for i in range(n):
                    if g[place][i] > 0:
                        heapq.heappush(heap, (price + g[place][i], i, remainStops - 1))
        
        return -1