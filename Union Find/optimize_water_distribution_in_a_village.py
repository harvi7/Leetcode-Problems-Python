class DSU:
    def __init__(self, size) -> None:
        self.size = [0] * (size + 1)
        self.root = [i for i in range(size + 1)]

    def find(self, x: int) -> int:
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False

        if self.size[rootX] < self.size[rootY]:
            self.root[rootX] = rootY
            self.size[rootY] += self.size[rootX];
        else:
            self.root[rootY] = rootX
            self.size[rootX] += self.size[rootY];
        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        heap = []
        for index, weight in enumerate(wells):
            heap.append((weight, 0, index + 1))

        for house_1, house_2, weight in pipes:
            heap.append((weight, house_1, house_2))

        heap.sort(key = lambda x: x[0])

        dsu = DSU(n)
        total_cost = 0
        for cost, house_1, house_2 in heap:
            if dsu.union(house_1, house_2):
                total_cost += cost

        return total_cost