class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = [0] * len(boxes)
        ops, balls = 0, 0
        for i in range(len(boxes)):
            ops += balls
            output[i] = ops
            balls += int(boxes[i])
        ops, balls = 0, 0
        for i in range(len(boxes)-1, -1, -1):
            ops += balls
            output[i] += ops
            balls += int(boxes[i])
        return output