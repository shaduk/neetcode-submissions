class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        countPath = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(row, col):
            nonlocal countPath
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 1 or (row, col) in visited:
                return 
            if row == ROWS - 1 and col == COLS - 1:
                countPath += 1
                return
            visited.add((row,col))
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            visited.remove((row, col))
        dfs(0, 0)
        return countPath
                

