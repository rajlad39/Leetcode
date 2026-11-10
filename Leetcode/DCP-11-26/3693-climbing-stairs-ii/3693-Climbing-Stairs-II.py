from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # Since costs is 1-indexed in description, let's pad it with a 0 at index 0 
        # so that costs[i] corresponds to step i directly.
        c = [0] + costs
        
        # dp[i] stores the minimum cost to reach step i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Start from step 0 with cost = 0
        
        for j in range(1, n + 1):
            # Check previous reachable steps: j-1, j-2, j-3
            for i in range(max(0, j - 3), j):
                jump_cost = c[j] + (j - i) ** 2
                dp[j] = min(dp[j], dp[i] + jump_cost)
                
        return dp[n]