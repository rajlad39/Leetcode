from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        
        # Calculate the sum of absolute differences from the median
        return sum(abs(x - median) for x in nums)