class StockSpanner:

    def __init__(self):
        self.minStack = []

    def next(self, price: int) -> int:
        counter = 1
        if self.minStack:
            for i in range(len(self.minStack)-1, -1, -1):
                if price >= self.minStack[i]:
                    counter += 1
                else:
                    break
        self.minStack.append(price)
        return counter

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)