class HitCounter:

    def __init__(self):
        self.store = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.store[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for val in range(timestamp, timestamp-300, -1):
            if val in self.store:
                total += self.store[val]
        return total
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
