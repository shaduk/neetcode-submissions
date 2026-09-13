class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = [0] * len(boxes)
        balls = 0
        ops = 0
        for i in range(len(boxes)):
            ops += balls
            output[i] = ops
            if boxes[i] == '1':
                balls += 1
        ops, balls = 0, 0
        for i in range(len(boxes)-1, -1, -1):
            ops += balls
            output[i] += ops
            if boxes[i] == '1':
                balls += 1
        return output