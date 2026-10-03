class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.min_val = [0] * (4 * n)
        self.max_val = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _push(self, node):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            
            self.min_val[2 * node] += val
            self.max_val[2 * node] += val
            self.lazy[2 * node] += val
            
            self.min_val[2 * node + 1] += val
            self.max_val[2 * node + 1] += val
            self.lazy[2 * node + 1] += val
            
            self.lazy[node] = 0

    def update(self, node, start, end, ql, qr, val):
        if ql <= start and end <= qr:
            self.min_val[node] += val
            self.max_val[node] += val
            self.lazy[node] += val
            return

        self._push(node)
        mid = (start + end) // 2
        if ql <= mid:
            self.update(2 * node, start, mid, ql, qr, val)
        if qr > mid:
            self.update(2 * node + 1, mid + 1, end, ql, qr, val)

        self.min_val[node] = min(self.min_val[2 * node], self.min_val[2 * node + 1])
        self.max_val[node] = max(self.max_val[2 * node], self.max_val[2 * node + 1])

    def find_first_zero(self, node, start, end, max_r):
        # Return -1 if range has no zero or goes beyond allowed right boundary
        if start > max_r or self.min_val[node] > 0 or self.max_val[node] < 0:
            return -1

        if start == end:
            return start

        self._push(node)
        mid = (start + end) // 2

        # Check left child first to get the smallest index L
        res = self.find_first_zero(2 * node, start, mid, max_r)
        if res != -1:
            return res

        return self.find_first_zero(2 * node + 1, mid + 1, end, max_r)


class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        st = SegmentTree(n)
        last_pos = {}
        max_len = 0

        for r in range(n):
            val = nums[r]
            prev_pos = last_pos.get(val, -1)
            delta = 1 if val % 2 == 0 else -1

            # Update diff for all left endpoints L in range (prev_pos, r]
            st.update(1, 0, n - 1, prev_pos + 1, r, delta)
            last_pos[val] = r

            # Find the smallest left index L <= r with diff == 0
            first_l = st.find_first_zero(1, 0, n - 1, r)
            if first_l != -1:
                max_len = max(max_len, r - first_l + 1)

        return max_len