class StockSpanner:

    def __init__(self):
        self.stk = []
        self.index = -1  

    def next(self, price: int) -> int:
        self.index += 1
        while self.stk and self.stk[-1][-1] <= price:
            self.stk.pop()
        
        if not self.stk:
            self.stk.append([self.index, price])
            return self.index + 1

        result = self.stk[-1][0]
        self.stk.append([self.index, price])
        return self.index - result