class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.storage:
            popped = self.storage[key]
            for i in range(len(popped)-1, -1, -1):
                if timestamp >= popped[i][0]:
                    return popped[i][1]
        return ""
