class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = collections.OrderedDict() 
        self.arr = []
        self.hits[0] = 0
        self.count = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.count +=1
        self.hits[timestamp] = self.count 
        self.arr.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        previous_time = max(0,timestamp - 300) 
        if previous_time not in self.hits:
            i = bisect.bisect_left(self.arr, previous_time)
            previous_time = self.arr[i - 1] if i else 0
        last_added_key = list(self.hits.keys())[-1] 
        
        hits = self.hits[last_added_key] - self.hits[previous_time]
        return(hits)
#     def __init__(self):
#         self.c = 0
#         self.od = OrderedDict()     

#     def hit(self, timestamp: int) -> None:
#         if timestamp not in self.od:
#             self.od[timestamp] = 1
#         else:
#             self.od[timestamp] += 1
#         self.getHits(timestamp)
#         self.c += 1

#     def getHits(self, timestamp: int) -> int:
#         while self.od and next(iter(self.od)) <= timestamp - 300:
#             self.c -= self.od.popitem(last=False)[1]
#         return self.c
