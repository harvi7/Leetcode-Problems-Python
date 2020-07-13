import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        
        pq = []
        for key, val in count.items():
            heapq.heappush(pq, (-val, key))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(pq)[1])
        return result