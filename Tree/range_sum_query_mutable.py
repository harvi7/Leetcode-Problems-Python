# https://www.youtube.com/watch?v=v_wj_mOAlig&feature=youtu.be

class NumArray:

    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.fen_tree = [0] * (self.size + 1)
        for i, val in enumerate(nums):
            self.increment(i, val)
            
    def get_parent(self, index):
        return index - (index & -index)
    
    def get_next(self, index):
        return index + (index & -index)
    
    def increment(self, index, val):
        index += 1
        while index < len(self.fen_tree):
            self.fen_tree[index] += val
            index = self.get_next(index)
            
    def sum(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.fen_tree[index]
            index = self.get_parent(index)               
        return res

    def update(self, i: int, val: int) -> None:
        delta = val - self.sumRange(i, i)
        self.increment(i, delta) 

    def sumRange(self, i: int, j: int) -> int:
        return self.sum(j) - self.sum(i - 1)