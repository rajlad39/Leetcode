import math


class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                val = nums[j]
                prod *= val
                g = val if g == 0 else math.gcd(g, val)
                l = (l // math.gcd(l, val)) * val

                if prod == l * g:
                    max_len = max(max_len, j - i + 1)

        return max_len