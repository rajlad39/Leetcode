from collections import deque
from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        def bfs(sr, sc):
            queue = deque([(sr, sc)])
            grid[sr][sc] = 1
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))
                        
        # Step 1: Flood all 0s connected to the boundary
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 0:
                    bfs(r, c)
                    
        # Step 2: Count remaining closed islands
        closed_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    closed_count += 1
                    bfs(r, c)
                    
        return closed_count