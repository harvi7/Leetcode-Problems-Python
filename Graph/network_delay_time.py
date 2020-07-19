# https://leetcode.com/problems/network-delay-time/discuss/187713/Python-concise-queue-and-heap-solutions

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        pq, dist, graph = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        while pq:
            time, node = heapq.heappop(pq)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    heapq.heappush(pq, (time + w, v))
        return max(dist.values()) if len(dist) == N else -1