class UnionFind(object):
    def __init__(self):
        self.parents = dict()
        self.sizes = dict()
        self.n = 0

    def __contains__(self, key):
        return key in self.parents
        
    def insert(self, r, c):
        if self.__contains__((r,c)): return
        self.parents[(r, c)] = (r, c)
        self.sizes[(r, c)] = 1
        self.n += 1
        
    def find(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])  
            i = self.parents[i]
        return i

    def union(self, p, q):
        root_p, root_q = map(self.find, (p, q))
        if root_p == root_q: return
        small, big = sorted([root_p, root_q], key=lambda x: self.sizes[x])
        self.parents[small] = big
        self.sizes[big] += self.sizes[small] 
        self.n -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind()
        num_islands = []
        for r, c in positions:
            uf.insert(r, c)
            for rr, cc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                if (rr, cc) not in uf: continue
                uf.union((r,c), (rr,cc))
            num_islands.append(uf.n)
        return num_islands     
