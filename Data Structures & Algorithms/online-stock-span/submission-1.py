class StockSpanner:

    def __init__(self):
        self.minStack = []

    def next(self, price: int) -> int:
        counter = 1
        while self.minStack and price >= self.minStack[-1][0]:
            counter += self.minStack[-1][1]
            self.minStack.pop()
        self.minStack.append((price, counter))
        return counter

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)