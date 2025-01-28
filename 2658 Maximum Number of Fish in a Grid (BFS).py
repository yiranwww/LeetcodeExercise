# Leetcode 2658 Maximum Number of Fish in a Grid
# using BFS
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    q = deque()
                    q.append((i, j))
                    f = grid[i][j]
                    grid[i][j] = 0
                    while q:
                        cur_x, cur_y = q.popleft()
                        for dx, dy in direction:
                            new_x = cur_x + dx
                            new_y = cur_y + dy
                            if (0 <= new_x < n) and (0<= new_y < m) and grid[new_x][new_y] > 0:
                                f += grid[new_x][new_y]
                                grid[new_x][new_y] = 0
                                q.append((new_x, new_y))
                    ans = max(ans, f)
        return ans
