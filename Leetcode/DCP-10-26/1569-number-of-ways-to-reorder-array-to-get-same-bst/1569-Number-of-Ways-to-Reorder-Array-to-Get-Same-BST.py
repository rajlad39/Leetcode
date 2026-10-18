from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Precompute binomial coefficients using Pascal's triangle
        c = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if j == 0 or j == i:
                    c[i][j] = 1
                else:
                    c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD
                    
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            left_ways = dfs(left)
            right_ways = dfs(right)
            
            # Ways to interleave left and right elements
            comb = c[len(left) + len(right)][len(left)]
            
            res = (comb * left_ways) % MOD
            res = (res * right_ways) % MOD
            return res

        return (dfs(nums) - 1 + MOD) % MOD