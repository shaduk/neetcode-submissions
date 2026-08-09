class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        minute = 0
        ROWL, COLL = len(grid), len(grid[0])

        for r in range(ROWL):
            for c in range(COLL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                (row, col) = queue.popleft()
                for index in ([0, 1], [1, 0], [-1, 0], [0, -1]):
                    newr, newc = row + index[0], col + index[1]
                    if newr < 0 or newc < 0 or newr >= ROWL or newc >= COLL or grid[newr][newc] == 0:
                        continue
                    if grid[newr][newc] == 1:
                        fresh -= 1
                        grid[newr][newc] = 2
                        queue.append((newr, newc))
            minute += 1
        if fresh == 0:
            return minute
        return -1