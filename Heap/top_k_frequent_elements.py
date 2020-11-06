class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for num, freq in collections.Counter(nums).items():
            if len(heap) >= k:
                heapq.heappushpop(heap, (freq, num))
            else:
                heapq.heappush(heap, (freq, num))
        
        return [num for freq, num in heap]