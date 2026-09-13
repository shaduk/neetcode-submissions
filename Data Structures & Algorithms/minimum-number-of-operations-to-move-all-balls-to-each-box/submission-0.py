class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = [0]*len(boxes)
        for i in range(0, len(boxes)):
            for j in range(0, len(boxes)):
                if boxes[j] == '1':
                    output[i] += abs(j-i)
        return output