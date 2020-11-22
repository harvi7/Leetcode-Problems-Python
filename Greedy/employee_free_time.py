class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        if not schedule: return []
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append([interval.start, interval.end])
                
        intervals.sort(key=lambda x: x[0])
        
        result = []
        lastEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
            
            if currStart > lastEnd:
                result.append(Interval(lastEnd, currStart))
            lastEnd = max(lastEnd, currEnd)
           
        return result