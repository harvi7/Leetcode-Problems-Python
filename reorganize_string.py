import collections
import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        counts = collections.Counter(S)
        result, maxheap = [], []
        last = None    
        for key in counts:
            heapq.heappush(maxheap, [-1 * counts[key], key]) 
        while maxheap:
            node = heapq.heappop(maxheap)     
            result.append(node[1])
            node[0] += 1                  
            if last and last[0] < 0:       
                heapq.heappush(maxheap, last)
            last = node  
        if len(result) == len(S):
            return "".join(result)
        else:
            return ""