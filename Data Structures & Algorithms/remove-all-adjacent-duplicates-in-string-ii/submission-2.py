class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 1]]
        for character in s:
            if stack[-1][0] == character:
                stack[-1][1] += 1
            else:
                stack.append([character, 1])
            if k == stack[-1][1]:
                stack.pop()
        return ''.join([c[0]*c[1] for c in stack[1:]])