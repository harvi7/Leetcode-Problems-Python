class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.col = 0
        self.row = 0
        self.v = v

    def next(self) -> int:
        self.updateCoors()
        self.col += 1
        return self.v[self.row][self.col - 1]

    def hasNext(self) -> bool:
        self.updateCoors()
        return self.row != len(self.v)
    
    def updateCoors(self):
        while self.row < len(self.v) and self.col == len(self.v[self.row]):
            self.row += 1
            self.col = 0
        
