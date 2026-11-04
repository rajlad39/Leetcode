from typing import List
import heapq

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        
        # Function to calculate the cost to make all elements in a window of size x equal.
        def get_costs():
            costs = [float('inf')] * (n + 1)
            for i in range(n - x + 1):
                window = sorted(nums[i:i + x])
                median = window[x // 2]
                cost = sum(abs(v - median) for v in window)
                costs[i + x] = cost
            return costs

        window_costs = get_costs()
        
        # dp[j][i] = min cost to get j subarrays using prefix of length i
        prev = [float('inf')] * (n + 1)
        prev[0] = 0
        
        for j in range(1, k + 1):
            curr = [float('inf')] * (n + 1)
            min_prev = float('inf')
            
            for i in range(j * x, n + 1):
                min_prev = min(min_prev, prev[i - x])
                if window_costs[i] != float('inf') and min_prev != float('inf'):
                    curr[i] = min_prev + window_costs[i]
                if i > 0:
                    curr[i] = min(curr[i], curr[i - 1])
            prev = curr
            
        return prev[n] if prev[n] != float('inf') else -1