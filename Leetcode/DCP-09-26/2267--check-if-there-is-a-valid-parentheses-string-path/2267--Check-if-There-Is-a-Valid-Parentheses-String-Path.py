class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Total path length must be even, start with '(', and end with ')'
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        max_open = (m + n - 1) // 2
        memo = {}
        
        def dfs(r: int, c: int, open_count: int) -> bool:
            open_count += 1 if grid[r][c] == '(' else -1
            
            if open_count < 0 or open_count > max_open:
                return False
            
            if r == m - 1 and c == n - 1:
                return open_count == 0
            
            state = (r, c, open_count)
            if state in memo:
                return memo[state]
            
            res = False
            if r + 1 < m:
                res = res or dfs(r + 1, c, open_count)
            if not res and c + 1 < n:
                res = res or dfs(r, c + 1, open_count)
                
            memo[state] = res
            return res
        
        return dfs(0, 0, 0)