class StockSpanner:

    def __init__(self):
        self.stk = []
        self.count = 1

    def next(self, price: int) -> int:
        if not self.stk:
            self.count = 1
            self.stk.append([price,self.count])
            self.count += 1
            return 1
        else:
            while self.stk and self.stk[-1][0] <= price:
                self.stk.pop()
            spn = self.count if not self.stk else self.count - self.stk[-1][1]
            self.stk.append([price,self.count])
            self.count += 1
            return spn



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)