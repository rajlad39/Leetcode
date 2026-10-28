from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[r][c] stores the set of all possible path XOR values reaching cell (r, c)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        dp[0][0].add(grid[0][0])
        
        for r in range(m):
            for c in range(n):
                # Transition from the cell above
                if r > 0:
                    for val in dp[r - 1][c]:
                        dp[r][c].add(val ^ grid[r][c])
                # Transition from the cell to the left
                if c > 0:
                    for val in dp[r][c - 1]:
                        dp[r][c].add(val ^ grid[r][c])
                        
        return min(dp[m - 1][n - 1])
        