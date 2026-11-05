from typing import List
import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        distance_count = 0
        n2 = len(arr2)
        
        for x in arr1:
            # Find the insertion point for x in arr2
            idx = bisect.bisect_left(arr2, x)
            
            # Check if any element in arr2 violates the condition |x - arr2[j]| <= d
            valid = True
            
            # Check the element just greater than or equal to x
            if idx < n2 and abs(arr2[idx] - x) <= d:
                valid = False
            
            # Check the element just smaller than x
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                valid = False
                
            if valid:
                distance_count += 1
                
        return distance_count