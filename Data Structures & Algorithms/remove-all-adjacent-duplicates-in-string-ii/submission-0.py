class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 1]]
        for character in s:
            popped = stack[-1]
            if stack[-1][0] == character:
                stack[-1][1] += 1
            else:
                stack.append([character, 1])
            if stack and k == stack[-1][1]:
                stack.pop()
        word = ''.join([c[0]*c[1] for c in stack])
        return word[1:]