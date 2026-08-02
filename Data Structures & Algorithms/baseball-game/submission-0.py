class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "+":
                val1, val2 = record[-1], record[-2]
                record.append(val1 + val2)
            elif op == "D":
                val = record[-1]
                record.append(2*val)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        return sum(record)