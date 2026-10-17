from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        # Store (digit_sum, num, original_index)
        items = [(get_digit_sum(nums[i]), nums[i], i) for i in range(n)]
        
        # Sort based on digit sum, then by the number itself
        items.sort(key=lambda x: (x[0], x[1]))
        
        # Map original index to its sorted target position
        mapping = [0] * n
        for i in range(n):
            orig_idx = items[i][2]
            mapping[orig_idx] = i
            
        # Count cycles in the permutation mapping
        visited = [False] * n
        cycles = 0
        
        for i in range(n):
            if not visited[i]:
                cycles += 1
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    curr = mapping[curr]
                    
        return n - cycles