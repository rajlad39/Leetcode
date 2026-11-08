from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        
        row_counts = [0] * m
        col_counts = [0] * n
        
        # Count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
                    
        communicating_servers = 0
        
        # Check each server
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_counts[i] > 1 or col_counts[j] > 1:
                        communicating_servers += 1
                        
        return communicating_servers