from collections import Counter


class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        mod1 = (1 << 61) - 1
        mod2 = 1_000_000_009
        base1 = 100003
        base2 = 100019

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i, val in enumerate(nums):
            x = val + 1
            pow1[i + 1] = (pow1[i] * base1) % mod1
            pow2[i + 1] = (pow2[i] * base2) % mod2
            pref1[i + 1] = (pref1[i] * base1 + x) % mod1
            pref2[i + 1] = (pref2[i] * base2 + x) % mod2

        def has_unique_of_len(k: int) -> bool:
            counts = Counter()
            p1 = pow1[k]
            p2 = pow2[k]
            for i in range(n - k + 1):
                h1 = (pref1[i + k] - pref1[i] * p1) % mod1
                h2 = (pref2[i + k] - pref2[i] * p2) % mod2
                counts[(h1, h2)] += 1
            return any(cnt == 1 for cnt in counts.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_len(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans