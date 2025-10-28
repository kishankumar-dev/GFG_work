from collections import deque
class Solution:
    def nearest(self, grid):
        n, m = len(grid), len(grid[0])
        q = deque()
        dist = [[-1 for _ in range(m)] for _ in range(n)]
        # Step 1: Push all cells having 1 into the queue
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dist[i][j] = 0  # distance to itself is 0
        # Step 2: Define 4 directions for BFS
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Step 3: BFS traversal
        while q:
            i, j = q.popleft()
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and dist[x][y] == -1:
                    dist[x][y] = dist[i][j] + 1
                    q.append((x, y))
        return dist