class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    ans = max(ans, self.dfs(i, j, grid, n, m))
        return ans



    def dfs(self, i, j, grid, n, m):
        f = grid[i][j]
        grid[i][j] = 0
        direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dx, dy in direction:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > 0:
                f += self.dfs(nx, ny, grid, n, m)
        return f
        
