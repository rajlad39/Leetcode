from collections import deque
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        c = nums[0]
        
        # Check if the array is a pure rotation of the sorted array
        is_rotation = True
        for i in range(n):
            if nums[i] != (c + i) % n:
                is_rotation = False
                break
                
        if is_rotation:
            start_rev = 0
            start_c = c
        else:
            # Check if the array is a reflection of the sorted array
            is_reflection = True
            for i in range(n):
                if nums[i] != (c - i) % n:
                    is_reflection = False
                    break
            if is_reflection:
                start_rev = 1
                start_c = c
            else:
                return -1  # Impossible to reach using the given operations
                
        target_rev = 0
        target_c = 0
        
        if start_rev == target_rev and start_c == target_c:
            return 0
            
        # BFS to find the shortest path in the 2n state space
        dist = [[-1] * n for _ in range(2)]
        dist[start_rev][start_c] = 0
        queue = deque([(start_rev, start_c)])
        
        while queue:
            rev, c = queue.popleft()
            d = dist[rev][c]
            
            if rev == target_rev and c == target_c:
                return d
                
            # Transition 1: Left Rotate (L)
            if rev == 0:
                n_rev, n_c = 0, (c + 1) % n
            else:
                n_rev, n_c = 1, (c - 1) % n
                
            if dist[n_rev][n_c] == -1:
                dist[n_rev][n_c] = d + 1
                queue.append((n_rev, n_c))
                
            # Transition 2: Reverse (R)
            if rev == 0:
                n_rev, n_c = 1, (c - 1) % n
            else:
                n_rev, n_c = 0, (c + 1) % n
                
            if dist[n_rev][n_c] == -1:
                dist[n_rev][n_c] = d + 1
                queue.append((n_rev, n_c))
                
        return -1