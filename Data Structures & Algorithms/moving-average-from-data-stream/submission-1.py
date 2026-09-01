from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.maxSize = size
        self.values = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.values.append(val)
        self.window_sum += val
        
        if len(self.values) > self.maxSize:
            self.window_sum -= self.values.popleft()
        
        return self.window_sum / len(self.values)