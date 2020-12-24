class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def taxi(P, Q):
            return abs(P[0] - Q[0]) + abs(P[1] - Q[1])

        return all(taxi([0, 0], target) < taxi(ghost, target)
               for ghost in ghosts)