from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Memoization for mirror reflection destinations:
        # resolve(r, c, dir_type) where dir_type: 0 = entered moving Right, 1 = entered moving Down
        # Returns (target_r, target_c, target_dir) or None if out of bounds
        memo = {}

        def resolve(r, c, d):
            if not (0 <= r < m and 0 <= c < n):
                return None
            if grid[r][c] == 0:
                return (r, c, d)
            
            state = (r, c, d)
            if state in memo:
                return memo[state]
            
            # If entered moving Right (d=0), reflect Down to (r+1, c) entering moving Down (d=1)
            # If entered moving Down (d=1), reflect Right to (r, c+1) entering moving Right (d=0)
            if d == 0:
                res = resolve(r + 1, c, 1)
            else:
                res = resolve(r, c + 1, 0)
                
            memo[state] = res
            return res

        # dp[r][c][0] -> paths reaching (r, c) moving Right
        # dp[r][c][1] -> paths reaching (r, c) moving Down
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        
        # Base state: Start at (0,0) with 1 way to be at (0,0)
        # We can seed it by pretending we entered (0,0) from both directions (summed at end)
        # Or more cleanly, process transitions directly from (0,0)
        dp[0][0][0] = 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    continue
                
                total_ways = (dp[r][c][0] + dp[r][c][1]) % MOD
                if total_ways == 0 and (r != 0 or c != 0):
                    continue
                
                # Base case start cell fix:
                ways = 1 if (r == 0 and c == 0) else total_ways
                
                # 1. Try moving Right to (r, c + 1)
                dest_right = resolve(r, c + 1, 0)
                if dest_right:
                    tr, tc, td = dest_right
                    dp[tr][tc][td] = (dp[tr][tc][td] + ways) % MOD
                
                # 2. Try moving Down to (r + 1, c)
                dest_down = resolve(r + 1, c, 1)
                if dest_down:
                    tr, tc, td = dest_down
                    dp[tr][tc][td] = (dp[tr][tc][td] + ways) % MOD

        return (dp[m - 1][n - 1][0] + dp[m - 1][n - 1][1]) % MOD