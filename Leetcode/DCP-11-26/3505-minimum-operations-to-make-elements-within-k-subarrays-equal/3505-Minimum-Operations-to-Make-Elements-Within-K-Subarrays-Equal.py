
from typing import List
from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)

        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            step >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        count = Fenwick(m)
        sums = Fenwick(m)

        total = 0
        cost = [0] * (n - x + 1)

        for i, v in enumerate(nums):
            pos = bisect_left(vals, v) + 1

            count.add(pos, 1)
            sums.add(pos, v)
            total += v

            if i >= x:
                old = nums[i - x]
                old_pos = bisect_left(vals, old) + 1

                count.add(old_pos, -1)
                sums.add(old_pos, -old)
                total -= old

            if i >= x - 1:
                mid_pos = count.kth((x + 1) // 2)
                median = vals[mid_pos - 1]

                left_count = count.query(mid_pos - 1)
                left_sum = sums.query(mid_pos - 1)

                right_count = x - count.query(mid_pos)
                right_sum = total - sums.query(mid_pos)

                cost[i - x + 1] = (
                    median * left_count - left_sum
                    + right_sum - median * right_count
                )

        INF = float('inf')

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]

                if i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + cost[i - x]
                    )

        return dp[n][k]
