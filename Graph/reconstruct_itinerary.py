# https://leetcode.com/problems/reconstruct-itinerary/discuss/375397/Simply-simple-Python-Solution-Using-stack-for-dfs-with-comments

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = {}
        for src, dst in tickets:
            if src in flights:
                flights[src].append(dst)
            else:
                flights[src] = [dst]

        for src in flights.keys():
            flights[src].sort(reverse=True)

        stack = []
        res = []
        stack.append("JFK")


        while len(stack) > 0:
            elem = stack[-1]
            if elem in flights and len(flights[elem]) > 0: 
                stack.append(flights[elem].pop())
            else:
                res.append(stack.pop())
        return res[::-1]