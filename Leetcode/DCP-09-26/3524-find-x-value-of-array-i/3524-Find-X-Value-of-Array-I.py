class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            
            # Start a new single-element subarray
            new_dp[num_mod] += 1
            
            # Extend existing subarrays ending at the previous element
            for r in range(k):
                if dp[r] > 0:
                    new_mod = (r * num_mod) % k
                    new_dp[new_mod] += dp[r]
            
            # Accumulate counts into the result array
            for r in range(k):
                ans[r] += new_dp[r]
            
            dp = new_dp
            
        return ans