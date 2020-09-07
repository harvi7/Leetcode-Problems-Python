class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_dict, max_gap = {}, 0
        for row in wall:
            brick_sum = 0
            for i in range(0, len(row) - 1):
                brick_sum += row[i]
                edge_dict[brick_sum] = edge_dict.get(brick_sum, 0) + 1
                max_gap = max(max_gap, edge_dict.get(brick_sum))
                
        return len(wall) - max_gap