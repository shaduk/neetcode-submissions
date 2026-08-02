class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                cellval = board[i][j]
                if cellval == ".":
                    continue
                elif cellval in row[i] or cellval in col[j] or cellval in squares[(i//3,j//3)]:
                    return False
                row[i].add(cellval)
                col[j].add(cellval)
                squares[(i//3,j//3)].add(cellval)
        return True