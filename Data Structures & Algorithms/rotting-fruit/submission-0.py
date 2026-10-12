class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                val = grid[r][c]
                if val == 1:    fresh += 1
                elif val == 2:  rot.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while rot and fresh > 0:
            for i in range(len(rot)):
                r, c = rot.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == len(grid) or 
                        col < 0 or col == len(grid[0])) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    rot.append((row, col))
            time += 1
        
        return time if fresh == 0 else -1

        