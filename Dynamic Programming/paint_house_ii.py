class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0: return 0 
        k = len(costs[0])

        prev_min_cost = prev_second_min_cost = prev_min_color = None
        for color, cost in enumerate(costs[0]):
            if prev_min_cost is None or cost < prev_min_cost:
                prev_second_min_cost = prev_min_cost
                prev_min_color = color
                prev_min_cost = cost
            elif prev_second_min_cost is None or cost < prev_second_min_cost:
                prev_second_min_cost = cost

        for house in range(1, n):
            min_cost = second_min_cost = min_color = None
            for color in range(k):
                cost = costs[house][color]
                if color == prev_min_color:
                    cost += prev_second_min_cost
                else:
                    cost += prev_min_cost
                if min_cost is None or cost < min_cost:
                    second_min_cost = min_cost
                    min_color = color
                    min_cost = cost
                elif second_min_cost is None or cost < second_min_cost:
                    second_min_cost = cost
            prev_min_cost = min_cost
            prev_min_color = min_color
            prev_second_min_cost = second_min_cost

        return prev_min_cost