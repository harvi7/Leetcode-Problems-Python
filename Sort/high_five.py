import collections
import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        allScores = collections.defaultdict(list)
        solution = []

        for id, score in items:
            heapq.heappush(allScores[id], -score)

        for id in allScores:
            avg_scores = sum(-heapq.heappop(allScores[id]) for i in range(0, 5)) // 5
            solution.append((id, avg_scores))

        return sorted(solution)