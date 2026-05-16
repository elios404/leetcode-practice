class StockSpanner:

    def __init__(self):
        self.idx = 1
        self.stack = []

    def next(self, price: int) -> int:
        while self.stack:
            if self.stack[-1][0] > price:
                break
            self.stack.pop()
        
        if not self.stack:
            ret = self.idx
        else:
            ret = self.idx - self.stack[-1][1]
        self.stack.append((price, self.idx))
        self.idx += 1

        return ret
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)