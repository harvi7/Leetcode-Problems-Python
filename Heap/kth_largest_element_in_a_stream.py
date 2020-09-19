class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = nums
        self.k = k
        heapq.heapify(self.pq)
        while len(self.pq) > k:
            heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
        elif val > self.pq[0]:
            heapq.heapreplace(self.pq, val)
        return self.pq[0]
