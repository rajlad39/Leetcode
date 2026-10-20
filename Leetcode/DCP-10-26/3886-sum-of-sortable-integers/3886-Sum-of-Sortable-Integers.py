from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Find all divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        divisors.sort()
        
        total_sum = 0
        
        # Step 2: Check each divisor k
        for k in divisors:
            possible = True
            min_vals = []
            max_vals = []
            
            # Partition into subarrays of length k
            for j in range(0, n, k):
                sub = nums[j:j+k]
                
                # Check drop count for cyclic sortability
                drops = 0
                for i in range(k):
                    if sub[i] > sub[(i + 1) % k]:
                        drops += 1
                        
                if drops > 1:
                    possible = False
                    break
                    
                min_vals.append(min(sub))
                max_vals.append(max(sub))
            
            if not possible:
                continue
                
            # Step 3: Check adjacent subarray conditions (max(S_i) <= min(S_{i+1}))
            for j in range(len(max_vals) - 1):
                if max_vals[j] > min_vals[j+1]:
                    possible = False
                    break
            
            if possible:
                total_sum += k
                
        return total_sum