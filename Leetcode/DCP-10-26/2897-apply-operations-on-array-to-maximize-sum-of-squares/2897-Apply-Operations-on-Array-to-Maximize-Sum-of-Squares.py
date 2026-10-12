class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 31
        
        # Count set bits at each position
        for x in nums:
            for i in range(31):
                if (x >> i) & 1:
                    cnt[i] += 1
        
        ans = 0
        # Greedily build the k largest numbers
        for _ in range(k):
            x = 0
            for i in range(31):
                if cnt[i] > 0:
                    x |= (1 << i)
                    cnt[i] -= 1
            ans = (ans + x * x) % MOD
            
        return ans