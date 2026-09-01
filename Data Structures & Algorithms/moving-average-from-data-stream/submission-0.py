class MovingAverage:

    def __init__(self, size: int):
        self.maxSize = size
        self.values = deque()

    def next(self, val: int) -> float:
        self.values.append(val)
        size = len(self.values)
        if size > self.maxSize:
            self.values.popleft()
            size -= 1
        return sum(self.values)/size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
