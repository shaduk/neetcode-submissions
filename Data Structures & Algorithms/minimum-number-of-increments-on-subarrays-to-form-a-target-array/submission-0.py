class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        if len(target) == 0:
            return
        result = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                result += target[i] - target[i-1]
        return result