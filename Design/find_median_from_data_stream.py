# https://leetcode.com/problems/find-median-from-data-stream/discuss/677080/Well-commented-python-code

class MedianFinder:

    def __init__(self):
        self.lowerhalf = [] 
        self.upperhalf = [] 

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.lowerhalf) == 0:
            heapq.heappush(self.lowerhalf, -num)
            return

        if num <= -self.lowerhalf[0]:
            heapq.heappush(self.lowerhalf, -num) 
        else:
            heapq.heappush(self.upperhalf, num) 
            
        if len(self.lowerhalf) - len(self.upperhalf) == 2:
            heapq.heappush(self.upperhalf, - heapq.heappop(self.lowerhalf))
        
        elif len(self.upperhalf) - len(self.lowerhalf) == 2:
            heapq.heappush(self.lowerhalf, - heapq.heappop(self.upperhalf))
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.lowerhalf) == len(self.upperhalf):
            return (- self.lowerhalf[0] + self.upperhalf[0] )/2.0 
        elif len(self.lowerhalf) > len(self.upperhalf):
            return -float(self.lowerhalf[0])
        else:
            return float(self.upperhalf[0])