# 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(r, c):
            if r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[r]) - 1 or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r, c + 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count