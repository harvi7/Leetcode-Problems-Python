class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = [[-1] * n for _ in range(n)]

        for edge in edges:
            graph[edge[0]][edge[1]] = edge[2]
            graph[edge[1]][edge[0]] = edge[2]
            
        ans  = 0

        visited = [False] * n

        pq = [[-maxMoves, 0]]

        while pq:
            nearestEl = heapq.heappop(pq)
            nearestNodeId = nearestEl[1]
            maxMovesRemaining = -nearestEl[0]
            if visited[nearestNodeId]:
                continue
            
            visited[nearestNodeId] = True

            ans += 1


            for nei in range(n):
                if graph[nearestNodeId][nei] != -1:
                    if not visited[nei] and (maxMovesRemaining >= graph[nearestNodeId][nei] + 1):
                        heapq.heappush(pq, [-(maxMovesRemaining - graph[nearestNodeId][nei] - 1), nei])

                    movesCost = min(maxMovesRemaining, graph[nearestNodeId][nei])

                    graph[nei][nearestNodeId] -= movesCost
                    graph[nearestNodeId][nei] -= movesCost

                    ans += movesCost

        return ans