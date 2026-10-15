from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        
        # Iterate over all possible starting points of subarrays
        for i in range(n):
            distinct_set = set()
            # Extend the subarray to each possible ending point
            for j in range(i, n):
                distinct_set.add(nums[j])
                # Square the count of distinct elements and add to total
                total += len(distinct_set) ** 2
                
        return total