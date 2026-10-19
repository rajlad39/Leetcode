from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Sort the array in non-decreasing order
        nums.sort()
        
        # Find and return all indices where the element equals the target
        return [i for i, x in enumerate(nums) if x == target]