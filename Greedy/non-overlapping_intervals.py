# https://www.youtube.com/watch?v=BW7LeuJIMhE&pbjreload=101

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2: return 0
        intervals.sort()
        count, last_included = 0, 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[last_included][1]: # Overlap
                count += 1
                if intervals[i][1] < intervals[last_included][1]: last_included = i
            else:
                last_included = i
        return count