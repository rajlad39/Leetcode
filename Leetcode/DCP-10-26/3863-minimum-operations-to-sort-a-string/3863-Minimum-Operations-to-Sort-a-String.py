from itertools import pairwise

class Solution:
    def minOperations(self, s: str) -> int:
        # Check if already sorted
        if all(a <= b for a, b in pairwise(s)):
            return 0
        
        # Length 2 cannot be changed with proper substrings if unsorted
        if len(s) == 2:
            return -1
            
        mn, mx = min(s), max(s)
        
        # If min is at the start or max is at the end
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # If min or max is in the interior
        if any(c in [mn, mx] for c in s[1:-1]):
            return 2
            
        return 3