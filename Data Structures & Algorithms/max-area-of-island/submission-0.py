class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def bfs(r, c):
            q = deque()
            area = 0
            q.append((r,c))

            while q:
                row, col = q.popleft()
                grid[row][col] = 0
                area += 1
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr < 0 or nc < 0 or nr > ROWS - 1 or nc > COLS - 1 or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea
        