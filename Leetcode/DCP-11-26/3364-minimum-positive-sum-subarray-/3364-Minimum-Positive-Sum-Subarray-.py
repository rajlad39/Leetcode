from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        # Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        min_sum = float('inf')
        
        # Check all possible subarray lengths from l to r
        for sz in range(l, r + 1):
            for i in range(n - sz + 1):
                j = i + sz
                sub_sum = prefix[j] - prefix[i]
                if sub_sum > 0:
                    min_sum = min(min_sum, sub_sum)
                    
        return min_sum if min_sum != float('inf') else -1