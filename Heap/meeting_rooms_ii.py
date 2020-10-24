class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) < 1: return 0
        
        intervals.sort()
        q = []
        
        for interval in intervals:
            if q and q[0] <= interval[0]:
                heapq.heappop(q)
            heapq.heappush(q, interval[1])
        return len(q)