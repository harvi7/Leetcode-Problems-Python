class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            if newInterval is None or interval[1] < newInterval[0]: 
                res.append(interval)
            elif newInterval[1] < interval[0]: 
                res.append(newInterval)
                res.append(interval)
                newInterval = None
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        if newInterval:
            res.append(newInterval)
        
        return res