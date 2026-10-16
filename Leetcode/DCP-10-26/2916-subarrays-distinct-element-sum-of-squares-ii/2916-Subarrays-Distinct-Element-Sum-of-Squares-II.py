from typing import List

class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.sum_d = [0] * (4 * n)
        self.sum_sq = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _push(self, node: int, start: int, end: int):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (start + end) // 2
            
            # Left child
            left = 2 * node
            len_l = mid - start + 1
            self.sum_sq[left] = (self.sum_sq[left] + 2 * val * self.sum_d[left] + val * val * len_l) % self.MOD
            self.sum_d[left] = (self.sum_d[left] + val * len_l) % self.MOD
            self.lazy[left] += val
            
            # Right child
            right = 2 * node + 1
            len_r = end - mid
            self.sum_sq[right] = (self.sum_sq[right] + 2 * val * self.sum_d[right] + val * val * len_r) % self.MOD
            self.sum_d[right] = (self.sum_d[right] + val * len_r) % self.MOD
            self.lazy[right] += val
            
            self.lazy[node] = 0

    def update(self, node: int, start: int, end: int, l: int, r: int, val: int):
        if l <= start and end <= r:
            length = end - start + 1
            self.sum_sq[node] = (self.sum_sq[node] + 2 * val * self.sum_d[node] + val * val * length) % self.MOD
            self.sum_d[node] = (self.sum_d[node] + val * length) % self.MOD
            self.lazy[node] += val
            return

        self._push(node, start, end)
        mid = (start + end) // 2
        if l <= mid:
            self.update(2 * node, start, mid, l, r, val)
        if r > mid:
            self.update(2 * node + 1, mid + 1, end, l, r, val)

        self.sum_d[node] = (self.sum_d[2 * node] + self.sum_d[2 * node + 1]) % self.MOD
        self.sum_sq[node] = (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]) % self.MOD

    def query_total_sq(self) -> int:
        return self.sum_sq[1]

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        st = SegmentTree(n)
        last_pos = {}
        ans = 0

        for j in range(n):
            val = nums[j]
            prev_idx = last_pos.get(val, -1)
            
            # Update range [prev_idx + 1, j] by +1
            st.update(1, 0, n - 1, prev_idx + 1, j, 1)
            
            # Accumulate the sum of squares for all valid starting positions i <= j
            ans = (ans + st.query_total_sq()) % MOD
            
            # Update last occurrence position
            last_pos[val] = j

        return ans