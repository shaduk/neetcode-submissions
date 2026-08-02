class MinStack:

    def __init__(self):
        self.minimum = []
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.minimum) == 0 or val <= self.minimum[-1]:
            self.minimum.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if len(self.minimum) != 0 and popped == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
